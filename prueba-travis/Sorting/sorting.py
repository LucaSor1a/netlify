class Sort():

    def BubleSort(self, Sort):
        n = len(Sort)
        for i in range(1, n):
            for j in range(n-1):
                if Sort[j] > Sort[j+1]:
                    Sort[j], Sort[j+1] = Sort[j+1], Sort[j]
        return Sort

    def InsertionSort(self, Sort):
        n = len(Sort)
        for i in range(1, n):
            val = Sort[i]
            j = i
            while j > 0 and Sort[j-1] > val:
                Sort[j] = Sort[j-1]
                j -= 1
            Sort[j] = val
        return Sort

    def MergeSort(self, Sort):
        if len(Sort) <= 1:
            return Sort
        medio = int(len(Sort) / 2)
        izquierda = self.MergeSort(Sort[:medio])
        derecha = self.MergeSort(Sort[medio:])
        return self.Merge(izquierda, derecha)

    def Merge(self, SortA, SortB):
        Sort_nueva = []
        a = 0
        b = 0
        while a < len(SortA) and b < len(SortB):
            if SortA[a] < SortB[b]:
                Sort_nueva.append(SortA[a])
                a += 1
            else:
                Sort_nueva.append(SortB[b])
                b += 1
        while a < len(SortA):
            Sort_nueva.append(SortA[a])
            a += 1
        while b < len(SortB):
            Sort_nueva.append(SortB[b])
            b += 1
        return Sort_nueva
