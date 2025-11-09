class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Cria um array de counts para armazenar os resultados.
        counts = [0] * n
        
        # Precisa rastrear o valor, o índice original e a contagem.
        #  Cria tuplas valor, indice_original
        items = []
        for i in range(n):
            items.append((nums[i], i))
            
        self.mergesort(items, counts)
        
        return counts

    def mergesort(self, items: list, counts: list) -> list:
       
        #  Caso Base 
        if len(items) <= 1:
            return items
            
        #  Dividir
        mid = len(items) // 2
        left_half = self.mergesort(items[:mid], counts)
        right_half = self.mergesort(items[mid:], counts)
        
        #  Combinar
        merged = []
        
        # Ponteiros para as metades esquerda (i) e direita (j)
        i, j = 0, 0
        
        # 'right_count' rastreia quantos elementos da direita
        # "pularam" para a esquerda (ou seja, são menores).
        right_count = 0
        
        while i < len(left_half) and j < len(right_half):
            # Caso 1: O elemento da direita é menor.
            # Este é uma inversão.
            if right_half[j][0] < left_half[i][0]:
                merged.append(right_half[j])
                right_count += 1
                j += 1
            # Caso 2: O elemento da esquerda é menor ou igual.
            # Não é uma inversão.
            else:
                # O elemento 'left_half[i]' é maior ou igual
                # a 'right_count' elementos da metade direita.
                # Adicionamos essa contagem ao seu índice original.
                
                original_index = left_half[i][1]
                counts[original_index] += right_count
                
                merged.append(left_half[i])
                i += 1
                
        # Pega os elementos restantes
        
        # Se sobraram elementos na esquerda
        while i < len(left_half):
            original_index = left_half[i][1]
            # Eles são maiores que TODOS os 'right_count' elementos da direita
            counts[original_index] += right_count
            
            merged.append(left_half[i])
            i += 1
            
        # Se sobraram elementos na direita não afeta as contagens
        while j < len(right_half):
            merged.append(right_half[j])
            j += 1
            
        return merged