'''
324. Wiggle Sort II: https://leetcode.com/problems/wiggle-sort-ii/description
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''
import random

class Solution:
    """
    Solução O(n) em tempo e O(1) em espaço.  Modifica 'nums' in-place.
    """
    def wiggleSort(self, nums: list[int]) -> None:
        
        n = len(nums)
        if n < 2:
            return

        # Encontra a Mediana
        k_index = (n - 1) // 2
        median = self.findKthSmallest_Iterative(nums, k_index)

        # Particionamento 3-Vias com Mapeamento Virtual
        
        # Função auxiliar para mapear o índice linear 'i' para o índice "wiggle" (ímpares primeiro, depois pares).
        def A(i):
            return (1 + 2 * i) % (n | 1)

        '''
        Particionamento 3-Vias (Algoritmo da Bandeira Holandesa)
        Objetivo:
        [ > median ] na "esquerda" virtual (índices 0..l-1 -> mapeados para 1, 3, 5...)
        [ == median] no "meio" virtual (índices l..m-1)
        [ < median ] na "direita" virtual (índices r+1..n-1 -> mapeados para ..., 4, 2, 0)
        '''
        
        l, m, r = 0, 0, n - 1
        
        while m <= r:
            mapped_m = A(m) # Índice virtual atual

            if nums[mapped_m] > median:
                # Se for MAIOR: move para a "esquerda" (início dos ímpares)
                mapped_l = A(l)
                nums[mapped_m], nums[mapped_l] = nums[mapped_l], nums[mapped_m]
                l += 1
                m += 1
            elif nums[mapped_m] < median:
                # Se for MENOR: move para a "direita" (final dos pares)
                mapped_r = A(r)
                nums[mapped_m], nums[mapped_r] = nums[mapped_r], nums[mapped_m]
                r -= 1
                # NÃO incrementamos 'm', o elemento trocado de 'r' precisa ser verificado.
            else:
                # Se for IGUAL: pertence ao "meio", apenas avançamos.
                m += 1
    
    
    def findKthSmallest_Iterative(self, nums: list[int], k: int) -> int:
        """
        Função QuickSelect. Encontra o k-ésimo menor elemento (0-indexado).
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            # Caso base da recursão.
            if l == r:
                return nums[l]

            # Escolhe um pivô aleatório
            pivot_idx = random.randint(l, r)
            
            # Particiona o subarray e obtém o índice final do pivô
            final_pivot_idx = self._partition(nums, l, r, pivot_idx)

            # Conquistar
            if final_pivot_idx == k:
                # Encontramos o elemento
                return nums[k]
            elif final_pivot_idx > k:
                # O k-ésimo elemento está na partição da esquerda. Apenas ajustamos o limite 'r'
                r = final_pivot_idx - 1
            else:
                # O k-ésimo elemento está na partição da direita. Apenas ajustamos o limite 'l'
                l = final_pivot_idx + 1
        
        return -1 # Não deve ser alcançado se k for válido

    def _partition(self, nums: list[int], l: int, r: int, pivot_idx: int) -> int:
        """
        Função auxiliar de particionamento. Move o pivô para sua posição final correta. Retorna o índice final do pivô.
        """
        pivot_val = nums[pivot_idx]
        
        # Move o pivô para o fim para facilitar
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        
        # 'store_idx' rastreia a fronteira dos elementos < pivô
        store_idx = l
        for i in range(l, r):
            if nums[i] < pivot_val:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Coloca o pivô em sua posição final correta
        nums[r], nums[store_idx] = nums[store_idx], nums[r]
        
        return store_idx