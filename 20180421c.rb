a = gets.split.map(&:to_i)
sum = 0
if a[0]+a[1] <= a[2]*2
  sum = a[0]*a[3]+a[1]*a[4]
else
  if a[3] < a[4]
    sum += a[3]*a[2]*2
    if a[1] <= a[2]*2
      sum += (a[4]-a[3])*a[1]
    else
      sum += (a[4]-a[3])*a[2]*2
    end
  else
    sum += a[4]*a[2]*2
    if a[0] <= a[2]*2
      sum += (a[3]-a[4])*a[0]
    else
      sum += (a[3]-a[4])*a[2]*2
    end
  end
end
puts sum

