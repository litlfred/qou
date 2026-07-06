The [tensor generation](#rem:simple-objects-V) property of the fundamental object $V$ has a concrete consequence for the hadron construction. Every constituent knot type $K_i$ in a [hadron](#def:hadron) factors through a tensor power of $V$.

Specifically, if $K_i$ is a knot whose associated simple object is $V_{j_i}$, then $V_{j_i}$ appears as a direct summand of $V^{\otimes 2j_i}$. The [PawLei basis](#prop:pawlowski-leitner-basis) provides a canonical embedding

$$
  \iota_{j_i} \colon V_{j_i}
   \hookrightarrow 
  V_{1/2}^{\otimes 2j_i},
$$

so a hadron $\mathfrak{H} \in V_{j_1} \otimes \cdots \otimes V_{j_n}$ can be written in a universal tensor form:

$$
  \mathfrak{H}  \hookrightarrow 
  V_{1/2}^{\otimes 2(j_1 + \cdots + j_n)}.
$$

This embedding is not unique. The choice of PawLei basis element for each factor corresponds to a choice of partial-wave channel. The physical hadron is obtained by summing over all channels weighted by the Skein polynomial. Thus, the [hadronic mass formula](#def:hadron) arises as a contraction of the universal tensor with the Hopf link invariant.

In the QOU framework, this factorization explains why all composite particles are ultimately built from the single two-dimensional object $V$. The categorical dimension $2$ of $V$ is the minimal non-trivial dimension compatible with the volume constraint. Tensor generation ensures no further building blocks are needed.
