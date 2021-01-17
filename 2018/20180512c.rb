s = gets
k = gets.to_i
t = []
a = 0
b = 0
while b < s.size-1
  a = 0
  while a <=b
    t << s[a..b]
    a+=1
  end
  b+=1
end
s =  t.uniq.sort
puts s[k-1]
