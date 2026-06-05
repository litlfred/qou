Let $V$ be the Gauss--Manin period space of the Seiberg--Witten family over
Bring's surface — the de Rham cohomology of the family, a finitely generated
free $R$-module of rank $r = \dim V \leq 2g = 8$. Let $M : V \to V$ be the
jet-prolongation operator ([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)),
$v_0 \in V$ the base period vector, and $\varphi : V \to R$ the period functional,
so $a_D^{(n)} = \varphi(M^n v_0)$.

*Cayley--Hamilton.* Because $V$ is finite-rank, $M$ satisfies its characteristic
polynomial: there is $d \leq r$ and coefficients $c_0,\dots,c_{d-1} \in R$ with
$M^d = \sum_{j<d} c_j\,M^j$.

*Operator recurrence.* For any $n$, using $M^{n+d} = M^n\!\cdot M^d$, the
Cayley--Hamilton relation, and distributivity of multiplication over the finite
sum,
$$
M^{n+d} = M^n\!\cdot\!\Big(\sum_{j<d} c_j M^j\Big)
        = \sum_{j<d} c_j\,(M^n\!\cdot M^j)
        = \sum_{j<d} c_j\,M^{n+j},
$$
where the middle step is `mul_smul_comm` (scalars commute past the operator
product) and the last is $M^n\!\cdot M^j = M^{n+j}$. This is the Lean theorem
[`QOU.Mass.prolongation_fixed_depth_recurrence`](#prop:prolonged-periods-fixed-depth),
verified sorry-free; the finite-rank premise (Cayley--Hamilton) is its
hypothesis.

*Period recurrence.* Applying the linear functional $T \mapsto \varphi(T v_0)$
to both sides and using its additivity and $R$-homogeneity (`map_sum`,
`map_smul`),
$$
a_D^{(n+d)} = \sum_{j<d} c_j\,a_D^{(n+j)},
$$
a depth-$d$ linear recurrence with $n$-independent kernel $c$. Hence a fixed-depth
recurrence on the prolonged periods exists, with depth bounded by
$\operatorname{rank} V$. Identifying $d$ and $c$ with the Bring Picard--Fuchs
operator is the remaining (identification) half of
[`conj:qdifference-kernel-prolongation-symbol`](#conj:qdifference-kernel-prolongation-symbol).
$\qquad\blacksquare$
