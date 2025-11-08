'''
493. Reverse Pairs: https://leetcode.com/problems/reverse-pairs/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Função recursiva que ordena o subarray arr[l...r] e retorna o número de 'reverse pairs' dentro desse subarray.
        """     
        def merge_sort_and_count(arr, l, r): 

            # Caso Base: se o subarray tem 0 ou 1 elemento, não há pares.
            if l >= r:
                return 0

            # Dividir: encontrar o ponto médio para dividir o array.
            mid = (l + r) // 2

            # Conquistar: chama recursivamente para as duas metades.
            # 'count' acumula os pares encontrados inteiramente dentro da metade esquerda ou inteiramente dentro da metade direita.
            count = merge_sort_and_count(arr, l, mid)
            count += merge_sort_and_count(arr, mid + 1, r)

            # Combinar (Contagem de Inversões): contamos os pares 'divididos', onde i está em [l, mid] e j está em [mid + 1, r]. Sabemos que arr[l...mid] e arr[mid+1...r] já estão ORDENADOS independentemente, graças às chamadas recursivas.
            j = mid + 1 # Ponteiro para a metade direita
            for i in range(l, mid + 1):
                '''
                'i' é o ponteiro para a metade esquerda
                Para cada 'i', avançamos 'j' até encontrar um elemento que NÃO satisfaça a condição.
                Como a metade direita está ordenada, todos os elementos antes de 'j' satisfazem a condição.
                '''
                while j <= r and arr[i] > 2 * arr[j]:
                    j += 1
                
                # O número de elementos válidos (j) encontrados na metade direita para o 'i' atual é (j - (mid + 1)).
                count += (j - (mid + 1))

            # Combinar: com o fim da contagem, fazemos uma mesclagem (merge) para que o array arr[l...r] fique totalmente ordenado para a chamada recursiva.
            temp = []
            ptr_l = l
            ptr_r = mid + 1

            while ptr_l <= mid and ptr_r <= r:
                if arr[ptr_l] <= arr[ptr_r]:
                    temp.append(arr[ptr_l])
                    ptr_l += 1
                else:
                    temp.append(arr[ptr_r])
                    ptr_r += 1
            
            # Adiciona os elementos restantes da primeira metade (se houver)
            while ptr_l <= mid:
                temp.append(arr[ptr_l])
                ptr_l += 1
                
            # Adiciona os elementos restantes da segunda metade (se houver)
            while ptr_r <= r:
                temp.append(arr[ptr_r])
                ptr_r += 1
            
            # Copia os elementos ordenados do 'temp' de volta para o array original
            for k in range(len(temp)):
                arr[l + k] = temp[k]
            
            # Retorna a contagem total para este nível
            return count

        # Inicia o processo para o array inteiro
        return merge_sort_and_count(nums, 0, len(nums) - 1)