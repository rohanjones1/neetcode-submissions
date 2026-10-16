class Solution:

  def numDecodings(self, s: str) -> int:
    # Any string starting with '0' cannot be decoded
    if not s or s[0] == "0":
      return 0

    # prev2 represents dp[i-2], prev1 represents dp[i-1]
    prev2 = 1  # Base case for empty string
    prev1 = 1  # Base case for single valid character

    for i in range(1, len(s)):
      curr = 0

      # Check 1-digit decoding (must not be '0')
      if s[i] != "0":
        curr += prev1

      # Check 2-digit decoding (must be between 10 and 26)
      two_digit = int(s[i - 1 : i + 1])
      if 10 <= two_digit <= 26:
        curr += prev2

      # If neither single nor two-digit decodings are valid, string cannot be decoded
      if curr == 0:
        return 0

      # Shift values for next iteration
      prev2, prev1 = prev1, curr

    return prev1