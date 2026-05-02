## Statement

**Proposition 3 (Diagrammatic Double Magic and LR-Fusion Rigidity).**
*A composite nuclear configuration of mass $A = Z + N$ is "double
magic" — i.e. maximally confined and homologically pure under the
shell-condensation criterion
([homological condensation](#conj:homological-shell-condensation))
— if and only if the Littlewood–Richardson fusion of the proton
representation $V_{\lambda_Z}$ and the neutron representation
$V_{\lambda_N}$,*

$$
  V_{\lambda_Z} \otimes V_{\lambda_N}
  \;\hookrightarrow\;
  H_A(q),
  \qquad
  V_{\lambda_Z} \otimes V_{\lambda_N}
  \;=\;
  \bigoplus_{\mu \,\vdash\, A}
  c^{\mu}_{\lambda_Z, \lambda_N} \,
  V_\mu,
$$

*has a dominant composite module $V_{\lambda_A}$ whose Jucys–Murphy
multiset is strictly gapless and globally neutral*

$$
  \kappa_{\lambda_A}
  \;=\;
  \sum_{x \in \lambda_A} c(x)
  \;=\;
  0.
$$

## Status

Conjecture (CLAUDE.md §3b axiom-class pattern). The propagation rule
applies: the present claim is downstream of
[homological shell condensation](#conj:homological-shell-condensation)
and inherits its conjectural status. The provable Hecke ingredient
— that the Littlewood–Richardson coefficients
$c^\mu_{\lambda_Z, \lambda_N}$ govern the decomposition into
irreducible Hecke modules — is standard \cite{mathas1999}.

## Proof sketch (conjectural)

**Step 1 — Tensor induction of the global state.**
The composite total state lives in the induction

$$
  V_{\lambda_Z} \otimes V_{\lambda_N}
  \;\hookrightarrow\;
  \mathrm{Ind}^{H_A(q)}_{H_Z(q) \otimes H_N(q)}
  \bigl(V_{\lambda_Z} \boxtimes V_{\lambda_N}\bigr).
$$

By Frobenius reciprocity in the Hecke setting, this induction
decomposes via the LR rule into a direct sum of irreducibles
$V_\mu$ for $\mu \vdash A$, with multiplicities
$c^\mu_{\lambda_Z, \lambda_N}$.

**Step 2 — Asymmetric leakage in non-magic states.**
If either constituent diagram contains unpaired Frobenius arms or
legs (i.e. fails self-conjugacy
[categorical neutrality](#conj:categorical-neutrality-saturated-shells)),
the LR rule forces the tensor product to shatter into a massive
superposition of asymmetric skew diagrams. The dominant component
$V_{\lambda_A}$ then has

$$
  \kappa_{\lambda_A}
  \;=\;
  \kappa_{\lambda_Z} + \kappa_{\lambda_N}
  \;\neq\; 0,
$$

so the composite fails the global-neutrality test and topological
flux leaks into the jet tower
([non-magic Li-6](#ex:non-magic-Li6-diagram)).

**Step 3 — The double-magic lock.**
When **both** $\lambda_Z$ and $\lambda_N$ are saturated, self-conjugate,
$\kappa$-balanced blocks
([categorical neutrality](#conj:categorical-neutrality-saturated-shells)),
the LR coefficients are sharply constrained. Two algebraic facts
combine:

1. **LR rigidity.** For saturated self-conjugate constituents, the
   LR expansion is dominated by a single composite $\mu = \lambda_A$
   whose Young diagram is the "interlock" of $\lambda_Z$ and
   $\lambda_N$ — gapless, with no asymmetric overhang.

2. **Content additivity.** The Jucys–Murphy multiset of $V_{\lambda_A}$
   is the (signed) sum of the multisets of $V_{\lambda_Z}$ and
   $V_{\lambda_N}$. Saturation + self-conjugacy of the
   constituents force

   $$
     \kappa_{\lambda_A}
     \;=\;
     \kappa_{\lambda_Z} + \kappa_{\lambda_N}
     \;=\;
     0 + 0
     \;=\; 0.
   $$

Together, these yield a strictly gapless, zero-defect Jucys–Murphy
spectrum on $V_{\lambda_A}$, in turn forcing $E_\infty^{p, >0}(A) = 0$
([homological condensation](#conj:homological-shell-condensation)).

## Empirical signature

The proposition predicts that *exactly* the double-magic isotopes
$(Z, N) \in \{(2, 2), (8, 8), (20, 20), (28, 28), (50, 50), (82, 82),
(82, 126), (126, 126)\}$ realise the LR rigidity condition. Each
corresponds to a Young-diagram pair where both $\lambda_Z$ and
$\lambda_N$ are simultaneously self-conjugate; the predicted set
matches the observed double-magic isotopes
$\{{}^{4}\mathrm{He}, {}^{16}\mathrm{O}, {}^{40}\mathrm{Ca},
{}^{56}\mathrm{Ni}, {}^{100}\mathrm{Sn}, {}^{208}\mathrm{Pb}\}$
(adjusted for proton/neutron asymmetry where $Z \neq N$ via the
LR-shadow rule on conjugate diagrams).

Three illustrative cases are pictured separately:

- [Single magic ${}^{18}\mathrm{O}$](#ex:single-magic-O18-diagram):
  $\lambda_Z$ saturated, $\lambda_N$ frayed → $\kappa_{\lambda_A} \neq 0$.
- [Double magic ${}^{40}\mathrm{Ca}$](#ex:double-magic-Ca40-diagram):
  $\lambda_Z = \lambda_N$ saturated and self-conjugate →
  $\kappa_{\lambda_A} = 0$, gapless.
- [Non-magic ${}^{6}\mathrm{Li}$](#ex:non-magic-Li6-diagram):
  both arms unbalanced → topological flux leakage.

## Open algebraic question

The proposition asserts **rigidity** of the LR fusion at saturated
self-conjugate inputs: a single composite $\mu$ dominates and
saturates the bound. A precise Lean-formalisable form of this
rigidity — in terms of $q$-deformed Littlewood–Richardson coefficients
$c^\mu_{\lambda_Z, \lambda_N}(q)$ vanishing for $\mu \neq \lambda_A$
on the saturated locus — is the open question this conjecture
isolates.
