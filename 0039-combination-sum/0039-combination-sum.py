class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # Sorting allows us to break early when candidates exceed the remaining target
        candidates.sort()

        def backtrack(start: int, current_path: list[int], remaining: int):
            if remaining == 0:
                res.append(current_path.copy())
                return

            for i in range(start, len(candidates)):
                # Pruning: since candidates is sorted, no subsequent numbers will fit
                if candidates[i] > remaining:
                    break
                
                # Choose the candidate
                current_path.append(candidates[i])
                
                # Pass `i` (not `i + 1`) because the same element can be reused unlimited times
                backtrack(i, current_path, remaining - candidates[i])
                
                # Backtrack: remove the candidate before trying the next one
                current_path.pop()

        backtrack(0, [], target)
        return res