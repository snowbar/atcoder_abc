input = gets.split
m = []
input[0].to_i.times{|n| m << gets.to_i}
sum = m.inject(0){|result,n| result + n}
puts (input[1].to_i - sum) / m.min + input[0].to_i
