n,k = gets.split.map(&:to_i)
place = gets.split.index{|item| item == "1"} 
count = 1
n -= k
while n>0
  n -= k-1
  count += 1
end
if place < k || place >= n-k || (place+1)%k == k-1 || (n-place+1)%k ==k-1
  puts count
else
  puts count+1
end

