'''
215. Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #Ponto de entrada: Encontrar o k-ésimo MAIOR é o mesmo que encontrar o (n-k)-ésimo MENOR.

        n = len(nums)
        # O índice que esta sendo procurando em um array ordenado (0-indexado)
        target_k_smallest_index = n - k
        
        # Chamas a função de Dividir e Conquistar
        return self.quickselect(nums, 0, n - 1, target_k_smallest_index)

    def quickselect(self, arr: list[int], left: int, right: int, k: int) -> int:
        
        #'k' é o índice-alvo que estamos procurando (k-ésimo menor).
        
        
        # Caso base: Se o subarray tem apenas um elemento, é ele.
        if left == right:
            return arr[left]
        
        # Escolha do Pivô
        # Escolhe um pivô aleatório no intervalo
        pivot_index = random.randint(left, right)
        pivot_value = arr[pivot_index]

        #  Conquistar
        # Divide o array em [< pivô], [== pivô], [> pivô]
        lt, gt = self.partition_3_way(arr, left, right, pivot_value)
        
        #  Combinar
        if k < lt:
            # O alvo está no bloco da esquerda (< pivô)
            return self.quickselect(arr, left, lt - 1, k)
        elif k > gt:
            # O alvo está no bloco da direita (> pivô)
            return self.quickselect(arr, gt + 1, right, k)
        else:
            # O alvo está no bloco do meio (== pivô)
            # O k-ésimo menor é o próprio pivô.
            return pivot_value

    def partition_3_way(self, arr: list[int], left: int, right: int, pivot_value: int) -> tuple[int, int]:
        """
        Particionamento de 3 Vias
        Organiza arr[left...right] em:
        - arr[left...lt-1]   < pivot_value
        - arr[lt...gt]       == pivot_value
        - arr[gt+1...right] > pivot_value
        
        Retorna (lt, gt) - os índices do bloco do meio [== pivô].
        """
        # Encontra o pivô e move para a esquerda (temporariamente)
        # para facilitar o algoritmo
        pivot_index = -1
        for i in range(left, right + 1):
            if arr[i] == pivot_value:
                pivot_index = i
                break
        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
        
        # P_lt: aponta para o fim do bloco "menor que"
        # P_gt: aponta para o início do bloco "maior que"
        # P_i:  iterador atual
        
        lt = left
        i = left + 1
        gt = right
        
        while i <= gt:
            if arr[i] < pivot_value:
                # Encontrou um < pivô
                # Joga ele para o bloco da esquerda
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot_value:
                # Encontrou um > pivô
                # Joga ele para o bloco da direita
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
                # NÃO incrementa 'i', pois o novo arr[i] (vindo da direita) ainda não foi processado.
            else:
                # Encontrou um == pivô
                # Deixa ele no meio e avança
                i += 1
                
        # O pivô original (que estava em 'left') está agora no final do bloco "menor que".
        # 'lt' aponta para o primeiro elemento que é "== pivô".
        # 'gt' aponta para o último elemento que é "== pivô".
        return (lt, gt)
