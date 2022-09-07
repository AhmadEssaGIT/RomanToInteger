# RomanToInteger
Simple Solution for the Roman to Integer exercise Using Python3 .


 
<pre>
  Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
</pre>

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
  
## Example 1:
<pre>
  > Input: num = 3
  > Output: "III"
  > Explanation: 3 is represented as 3 ones
</pre>

## Example 2:
<pre>
  > Input: s = "LVIII"
  > Output: 58
  > Explanation: L = 50, V= 5, III = 3
</pre>
## Example 3:
<pre>
  > Input: s = "MCMXCIV"
  > Output: 1994
  > Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

## Constraints:

    > 1 <= s.length <= 15 <br>
    > s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').<br>
    > It is guaranteed that s is a valid roman numeral in the range [1, 3999].
