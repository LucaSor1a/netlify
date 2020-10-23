/// when animating on canvas, it is best to use requestAnimationFrame instead of setTimeout or setInterval
// not supported in all browsers though and sometimes needs a prefix, so we need a shim
window.requestAnimFrame = ( function() {
	return window.requestAnimationFrame ||
				window.webkitRequestAnimationFrame ||
				window.mozRequestAnimationFrame ||
				function( callback ) {
					window.setTimeout( callback, 1000 / 60 );
				};
})();

// now we will setup our basic variables for the demo
var canvas = document.getElementById( 'canvas' ),
		ctx = canvas.getContext( '2d' ),
		// full screen dimensions
		w = window.innerWidth,
		h = window.innerHeight,
		// firework collection
		fireworks = [],
		// particle collection
		particles = [],
		// starting hue
		hue = 120,
		// when launching fireworks with a click, too many get launched at once without a limiter, one launch per 5 loop ticks
		limiterTotal = 5,
		limiterTick = 0,
		// this will time the auto launches of fireworks, one launch per 80 loop ticks
		timerTotal = 15,
		timerTick = 0,

    //This turn off the snow
    uwu = 0;

// set canvas dimensions
canvas.width = w;
canvas.height = h;

// now we are going to setup our function placeholders for the entire demo

// get a random number within a range
function random( min, max ) {
	return Math.random() * ( max - min ) + min;
}


// calculate the distance between two points
function calculateDistance( p1x, p1y, p2x, p2y ) {
	var xDistance = p1x - p2x,
			yDistance = p1y - p2y;
	return Math.sqrt( Math.pow( xDistance, 2 ) + Math.pow( yDistance, 2 ) );
}

// create firework
function Firework( sx, sy, tx, ty ) {
	// actual coordinates
	this.x = sx;
	this.y = sy;
	// starting coordinates
	this.sx = sx;
	this.sy = sy;
	// target coordinates
	this.tx = tx;
	this.ty = ty;
	// distance from starting point to target
	this.distanceToTarget = calculateDistance( sx, sy, tx, ty );
	this.distanceTraveled = 0;
	// track the past coordinates of each firework to create a trail effect, increase the coordinate count to create more prominent trails
	this.coordinates = [];
	this.coordinateCount = 3;
	// populate initial coordinate collection with the current coordinates
	while( this.coordinateCount-- ) {
		this.coordinates.push( [ this.x, this.y ] );
	}
	this.angle = Math.atan2( ty - sy, tx - sx );
	this.speed = 2;
	this.acceleration = 1.025;
	this.brightness = random( 50, 70 );
}

// update firework
Firework.prototype.update = function( index ) {
	// remove last item in coordinates array
	this.coordinates.pop();
	// add current coordinates to the start of the array
	this.coordinates.unshift( [ this.x, this.y ] );


	// speed up the firework
	this.speed *= this.acceleration;

	// get the current velocities based on angle and speed
	var vx = Math.cos( this.angle ) * this.speed,
			vy = Math.sin( this.angle ) * this.speed;
	// how far will the firework have traveled with velocities applied?
	this.distanceTraveled = calculateDistance( this.sx, this.sy, this.x + vx, this.y + vy );

	// if the distance traveled, including velocities, is greater than the initial distance to the target, then the target has been reached
	if( this.distanceTraveled >= this.distanceToTarget ) {
		createParticles( this.tx, this.ty );
		// remove the firework, use the index passed into the update function to determine which to remove
		fireworks.splice( index, 1 );
	} else {
		// target not reached, keep traveling
		this.x += vx;
		this.y += vy;
	}
}

// draw firework
Firework.prototype.draw = function() {
	ctx.beginPath();
	// move to the last tracked coordinate in the set, then draw a line to the current x and y
	ctx.moveTo( this.coordinates[ this.coordinates.length - 1][ 0 ], this.coordinates[ this.coordinates.length - 1][ 1 ] );
	ctx.lineTo( this.x, this.y );
	ctx.strokeStyle = 'hsl(' + hue + ', 100%, ' + this.brightness + '%)';
	ctx.stroke();

	ctx.beginPath();
	// draw the target for this firework with a pulsing circle
	ctx.arc( this.tx, this.ty, this.targetRadius, 0, Math.PI * 2 );
	ctx.stroke();
}

// create particle
function Particle( x, y ) {
	this.x = x;
	this.y = y;
	// track the past coordinates of each particle to create a trail effect, increase the coordinate count to create more prominent trails
	this.coordinates = [];
	this.coordinateCount = 10;
	while( this.coordinateCount-- ) {
		this.coordinates.push( [ this.x, this.y ] );
	}
	// set a random angle in all possible directions, in radians
	this.angle = random( 0, Math.PI * 2 );
	this.speed = random( 1, 10 );
	// friction will slow the particle down
	this.friction = 0.94;
	// gravity will be applied and pull the particle down
	this.gravity = 1;
	// set the hue to a random number +-50 of the overall hue variable
	this.hue = random( hue - 50, hue + 50 );
	this.brightness = random( 50, 80 );
	this.alpha = 7;
	// set how fast the particle fades out
	this.decay = random( 0.03, 0.09 );
}

// update particle
Particle.prototype.update = function( index ) {
	// remove last item in coordinates array
	this.coordinates.pop();
	// add current coordinates to the start of the array
	this.coordinates.unshift( [ this.x, this.y ] );
	// slow down the particle
	this.speed *= this.friction;
	// apply velocity
	this.x += Math.cos( this.angle ) * this.speed;
	this.y += Math.sin( this.angle ) * this.speed + this.gravity;
	// fade out the particle
	this.alpha -= this.decay;

	// remove the particle once the alpha is low enough, based on the passed in index
	if( this.alpha <= this.decay ) {
		particles.splice( index, 1 );
	}
}

// draw particle
Particle.prototype.draw = function() {
	ctx. beginPath();
	// move to the last tracked coordinates in the set, then draw a line to the current x and y
	ctx.moveTo( this.coordinates[ this.coordinates.length - 1 ][ 0 ], this.coordinates[ this.coordinates.length - 1 ][ 1 ] );
	ctx.lineTo( this.x, this.y );
	ctx.strokeStyle = 'hsla(' + this.hue + ', 100%, ' + this.brightness + '%, ' + this.alpha + ')';
	ctx.stroke();
}

// create particle group/explosion
function createParticles( x, y ) {
	// increase the particle count for a bigger explosion, beware of the canvas performance hit with the increased particles though
	var particleCount = 250;
	while( particleCount-- ) {
		particles.push( new Particle( x, y ) );
	}
}

// main demo loop
function loop() {
	// this function will run endlessly with requestAnimationFrame
	requestAnimFrame( loop );

	// increase the hue to get different colored fireworks over time
	//hue += 0.5;

  // create random color
  hue= random(0, 360 );

	// normally, clearRect() would be used to clear the canvas
	// we want to create a trailing effect though
	// setting the composite operation to destination-out will allow us to clear the canvas at a specific opacity, rather than wiping it entirely
	ctx.globalCompositeOperation = 'destination-out';
	// decrease the alpha property to create more prominent trails
	ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
	ctx.fillRect( 0, 0, w, h );
	// change the composite operation back to our main mode
	// lighter creates bright highlight points as the fireworks and particles overlap each other
	ctx.globalCompositeOperation = 'lighter';

	// loop over each firework, draw it, update it
	var i = fireworks.length;
	while( i-- ) {
		fireworks[ i ].draw();
		fireworks[ i ].update( i );
	}

	// loop over each particle, draw it, update it
	var i = particles.length;
	while( i-- ) {
		particles[ i ].draw();
		particles[ i ].update( i );
	}

	// launch fireworks automatically to random coordinates
	if( timerTick >= timerTotal ) {
			// start the firework at the bottom middle of the screen, then set the random target coordinates, the random y coordinates will be set within the range of the top half of the screen
			fireworks.push( new Firework( w / 2, h / 2, random( 0, w ), random( 0, h ) ) );
			timerTick = 0;
	} else {
		timerTick++;
	}


}









function getNextDate() {
	var fecha = new Date();
    var y = fecha.getFullYear();
	var m = fecha.getMonth();
	var d = fecha.getDate();
	var date = new Date();
	date.setFullYear(y);
	date.setHours(0);
	date.setMinutes(0);
	date.setSeconds(0);
	if ((m == 0 && d < 2) || (m == 11 && d >25)) {
		if (m == 0) {
			date.setFullYear(y + 1);
		}
		date.setMonth(0);
		date.setDate(1);
	} else {
		date.setMonth(11);
		date.setDate(25);
	}
	return date;
};

// Update the count down every 1 second
var xx = setInterval(function() {

  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var fiesta = getNextDate();
  var distance = fiesta.getTime() - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("demo").innerHTML = "Cuenta regresiva:" + "<br />" + "<br />" + days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (distance <= 0) {
	clearInterval(xx);
	if (fiesta.getMonth() == 0){
		document.getElementById("demo").innerHTML = "Feliz Año Nuevo!!!";
	} else {
		document.getElementById("demo").innerHTML = "Feliz Navidad!!!";
	}
    requestAnimFrame( loop );
		uwu = 1;
  }
}, 1000);





var random_background = '"./Cuenta atras/' + (Math.floor(Math.random() * 4) + 1) + '.jpg"';
document.getElementById('cool').style.background = "url(" + random_background + ")"; 















  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  var particlesOnScreen = 245;
  var particlesArray = [];
  var w,h;
  w = canvas.width = window.innerWidth;
  h = canvas.height = window.innerHeight;

  function random(min, max) {
      return min + Math.random() * (max - min + 1);
  };

  function clientResize(ev){
      w = canvas.width = window.innerWidth;
      h = canvas.height = window.innerHeight;
  };
  window.addEventListener("resize", clientResize);

  function createSnowFlakes() {
      for(var i = 0; i < particlesOnScreen; i++){
          particlesArray.push({
              x: Math.random() * w,
              y: Math.random() * h,
              opacity: Math.random(),
              speedX: random(-3, 3),
              speedY: random(1, 5),
              radius:random(0.5, 4.2),
          })
      }
  };

  function drawSnowFlakes(){
      for(var i = 0; i < particlesArray.length; i++){
          var gradient = ctx.createRadialGradient(
              particlesArray[i].x,
              particlesArray[i].y,
              0,
              particlesArray[i].x,
              particlesArray[i].y,
              particlesArray[i].radius
              );

              gradient.addColorStop(0, "rgba(255, 255, 255," + particlesArray[i].opacity + ")");  // white
              gradient.addColorStop(.8, "rgba(210, 236, 242," + particlesArray[i].opacity + ")");  // bluish
              gradient.addColorStop(1, "rgba(237, 247, 249," + particlesArray[i].opacity + ")");   // lighter bluish

              ctx.beginPath();
              ctx.arc(
              particlesArray[i].x,
              particlesArray[i].y,
              particlesArray[i].radius,
              0,
              Math.PI*2,
              false
              );

          ctx.fillStyle = gradient;
          ctx.fill();
      }
  };

  function moveSnowFlakes(){

      for (var i = 0; i < particlesArray.length; i++) {
          particlesArray[i].x += particlesArray[i].speedX;
          particlesArray[i].y += particlesArray[i].speedY;

          if (particlesArray[i].y > h) {
              particlesArray[i].x = Math.random() * w * 1.5;
              particlesArray[i].y = -50;
          }
      }
  };

  function updateSnowFall  () {
    if (uwu !== 1) {
      ctx.clearRect(0, 0, w, h);
      drawSnowFlakes();
      moveSnowFlakes();
    }
  };

  setInterval(updateSnowFall,50);
  createSnowFlakes();
