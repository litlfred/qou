## Physical identification

| Parameter | Irrep | Observable | What it fixes |
|:---:|:---:|:---:|:---|
| $\alpha_1$ | $(3)$ symmetric | $m_\mu/m_e$ | Aether $q_0$ (all crossings $+q$) |
| $\alpha_2$ | $(2,1)$ standard | $m_e$ | Mass scale (mixed eigenvalues) |
| $\alpha_3$ | $(1{,}1{,}1)$ alternating | $\mathfrak{Q}_\beta(n)$ | Interaction scale (all crossings $-q^{-1}$) |

The symmetric sector sees only $+q$ eigenvalues — it controls
the **shape** of the universe (how far $q$ is from $1$).
The alternating sector sees only $-q^{-1}$ eigenvalues — it
controls the **interaction strength** (the antisymmetric
channel that drives beta decay).  The standard sector mixes
both eigenvalues — it controls the **mass scale** (the
conversion between Hecke algebra units and MeV).

## Sufficiency of three parameters for all $A$

Nuclear computations at Level 0 use $H_A(R, q)$ (one strand per
nucleon), which for $A > 3$ has more than three irreps.
However, the typed crossing operators
([typed crossing operator](#def:typed-crossing-operator))
$C(\mathfrak{p}, \mathfrak{p})$, $C(\mathfrak{p}, \mathfrak{n})$,
$C(\mathfrak{n}, \mathfrak{n})$ are determined entirely by the
three $H_3(R, q)$ parameters:

$$
  C(\mathfrak{p}, \mathfrak{p}) = \sigma \quad (d = 0),
  \qquad
  C(\mathfrak{n}, \mathfrak{n}) = \sigma - h \quad (d = -h),
  \qquad
  C(\mathfrak{p}, \mathfrak{n}) = \sigma - h/2 \quad (d = -h/2).
$$

These three crossing types span all possible nucleon-nucleon
interactions.  The coefficients $(0, -h, -h/2)$ are fixed by
$q$ alone (via $h = q - q^{-1}$), and the energy scale $E_0$
converts NF differences to MeV.  No additional parameters
appear at higher $A$ because the $H_A(R, q)$ computation
factorizes through these three crossing types.

## Cross-check: leptonic sector

For $H_2(R, q)$ (two strands, leptonic physics):
- Partitions of $2$: $(2)$ and $(1{,}1)$
- $H_2(R, q) \cong k \oplus k$, $\dim = 1^2 + 1^2 = 2$
- Two irreps $\to$ two parameters ($q_0$ and $m_e$)
- No standard representation $\to$ no interaction scale needed

Leptonic physics requires only two inputs. The third input ($\mathfrak{Q}_\beta$) is needed only when matter and antimatter crossings coexist within a composite (hadrons).
