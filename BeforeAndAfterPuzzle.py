from collections import defaultdict
input = [
    'mission statement',
    'a quick bite to eat',
    'a chip off the old block',
    'chocolate bar',
    'mission impossible',
    'a man on a mission',
    'block party',
    'eat my words',
    'bar of soap'
]

end_word = defaultdict(list)
for i,s in enumerate(input):
    index = s.find(' ')
    if index == -1:
        end_word[s] += i,
    else:
        end_word[s[:index]] += i,
ans = []
for i,s in enumerate(input):
    index = s.rfind(' ')
    if index == -1:
       for idx in end_word[s]:
           if idx != i:
               ans.append(input[idx])
    else:
        for idx in end_word[s[index+1:]]:
            if idx != i:
                ans.append(s[:index+1] + input[idx])
print(ans)
