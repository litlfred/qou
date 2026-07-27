import math
Q = 2.277455
B2 = 2.224566
K = 1.0/32.0

print("B2 / Q = ", B2 / Q)
print("1 - K = ", 1 - K)
print("1 - K + K^2 = ", 1 - K + K**2)
print("1 - K + K^2 - K^3 = ", 1 - K + K**2 - K**3)

print("Q - B2 = ", Q - B2)
print("Q*K = ", Q*K)
print("Q*K - (Q-B2) = ", Q*K - (Q-B2))
print("(Q*K - (Q-B2))/Q = ", (Q*K - (Q-B2))/Q)
print("(Q*K - (Q-B2)) / (Q*K^2) = ", (Q*K - (Q-B2)) / (Q*K**2))

print("Is it Q * (1 - K + 8*K^2) ?")
print(Q * (1 - K + 8*K**2))

print("Let's look at the NA Stokes algebra.")
# exp(A) exp(B) = exp(A + B + 1/2 [A,B] + 1/12 [A,[A,B]] - 1/12 [B,[A,B]] + ...)
# If A and B are of order K, the commutator is order K^2.
