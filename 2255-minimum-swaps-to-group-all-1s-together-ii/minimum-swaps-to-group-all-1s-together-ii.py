class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)

        if ones <= 1:
            return 0

        nums = nums + nums

        zeros = ones - sum(nums[:ones])
        answer = zeros

        for i in range(ones, len(nums)):
            if nums[i] == 0:
                zeros += 1

            if nums[i - ones] == 0:
                zeros -= 1

            answer = min(answer, zeros)

        return answer