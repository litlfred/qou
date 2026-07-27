import itertools

B2 = 2.224566
Q = 2.277455
K = 1.0/32.0
E0 = 4.004
me = 0.51099895
pi = 3.141592653589793

constants = [('Q', Q), ('K', K), ('E0', E0), ('me', me), ('pi', pi), ('1', 1.0), ('2', 2.0)]
operations = ['+', '-', '*', '/']

def build_expr(depth):
    if depth == 0:
        for c in constants:
            yield c[0], c[1]
    else:
        for l_str, l_val in build_expr(depth - 1):
            for r_str, r_val in build_expr(depth - 1):
                for op in operations:
                    if op == '+':
                        yield f"({l_str} + {r_str})", l_val + r_val
                    elif op == '-':
                        yield f"({l_str} - {r_str})", l_val - r_val
                    elif op == '*':
                        yield f"({l_str} * {r_str})", l_val * r_val
                    elif op == '/':
                        if r_val != 0:
                            yield f"({l_str} / {r_str})", l_val / r_val

matches = []
# Just do a targeted search for a simpler structure like: Q * (1 - c*K) or Q - c*K*something
diff = Q - B2 # 0.052889
print("Q - B2 =", diff)
print("diff / K =", diff / K) # 1.692448
print("diff / (K * me) =", diff / (K * me)) # 3.312038
print("diff / (K * Q) =", diff / (K * Q)) # 0.743131

# Maybe Q * (1 - K) is the base, and there is a next order correction.
# Q * (1 - K) = 2.2062845...
diff2 = B2 - Q * (1 - K) # 0.018281468
print("B2 - Q*(1-K) =", diff2)
print("diff2 / K^2 =", diff2 / (K**2)) # 18.72022
print("diff2 / (K * me) =", diff2 / (K * me)) # 1.14488
print("diff2 / K =", diff2 / K) # 0.58500
