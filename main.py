def print_table(table):
   for x in range(len(table)):
      print(table[x])


def get_steps(table, s, c):
   ls = len(s) + 1
   lc = len(c) + 1
   x = ls - 1
   y = lc - 1
   steps = []

   while x > 0 and y > 0:
      # get our totals
      sub = table[x - 1][y - 1]
      add = table[x][y - 1]
      rem = table[x - 1][y]
      if sub <= add and sub <= rem:
         x -= 1
         y -= 1
         if s[x] != c[y]:
            steps.append("Substitute letter " + s[x] + " for " + c[y] + " at position " + str(x))
      elif add <= rem and add <= sub:
         y -= 1
         if s[x - 1] != c[y]:
            steps.append("Add letter " + c[y] + " at position " + str(y))
      else:
         x -= 1
         if s[x] != c[y - 1]:
            steps.append("Remove letter " + s[x] + " at position " + str(x))

   while x > 0:
      x -= 1
      steps.append("Remove letter " + s[x] + " at position " + str(x))
   while y > 0:
      y -= 1
      steps.append("Add letter " + c[y] + " at position " + str(y))

   return steps


def min_edit_distance(s, c):
   ls = len(s) + 1
   lc = len(c) + 1
   table = [[0] * lc for i in range(ls)]

   # make initial values in table
   for i in range(ls):
      table[i][0] = i
   for i in range(lc):
      table[0][i] = i

   for x in range(1, ls):
      for y in range(1, lc):
         table[x][y] = min(table[x - 1][y], table[x][y - 1], table[x - 1][y - 1])

         if s[x - 1] != c[y - 1]:
            table[x][y] = table[x][y] + 1

   steps = get_steps(table, s, c)
   if len(steps) > 0:
      for index, step in enumerate(steps):
         print(str(index+1) + ") " + step)
   else:
      print("No steps")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   min_edit_distance("bams", "sam")