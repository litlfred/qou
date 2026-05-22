The inter-nucleon binding operator is **not fixed** — it transitions
between three distinct regimes as the nucleus grows.  The
$\mathcal{B}_3$ confinement operator acts at the quark level only;
at the nuclear level, the demand-minimizing operator changes at
shell boundaries.

## Statement

**Proposition.**
*In the inductive construction of $\mathcal{N}(Z, N)$
([derived atom](#def:derived-atom)), the optimal inter-nucleon
binding operator $\Phi_k$ at step $k$ (adding nucleon $k+1$ to
nucleus $\mathcal{N}_{\leq k}$) belongs to one of three regimes:*

**(Regime I — Shell filling).**
*Within the first nuclear shell ($A \leq 2$ for $1s$), the
demand-minimizing operator is the torus knot $T_{2,n_s}$ where
$n_s$ is the shell size:*

$$
  \Phi_k = T_{2,5} = (\sigma_0\sigma_1)^2\sigma_0
  \qquad (k = 1,\; p \to pp)
$$

**(Regime II — Magic shell closure).**
*At and immediately after a magic number ($Z$ or $N \in \{2, 8, 20, 28, \ldots\}$),
the optimal operator is a Hopf link $L_\pm$:*

$$
  \Phi_k \in \{L_+ = \sigma_0\sigma_1,\; L_- = \sigma_1\sigma_0\}
$$

*The Hopf link achieves demand closure ($|\mathrm{dem}| = 0$) at
magic shell boundaries.  At doubly magic nuclei ($Z$ and $N$ both
magic), $L_+$ is selected for both the proton and neutron shell
closures.*

**(Regime III — Open shell).**
*Beyond a closed magic shell, the optimal operator reverts to the
bare typed crossing:*

$$
  \Phi_k \in \{C_{pp},\; C_{pn},\; C_{nn}\}
$$

*These are the standard inter-nucleon Hopf crossings
(positive, mixed, or negative typed).*

## Observed transitions for $A \leq 6$

| Step | Nucleons | Selected $\Phi_k$ | Regime | $|\mathrm{dem}|$ |
|:---|:---|:---|:---:|---:|
| $p \to pp$ | 1 $\to$ 2 | $T_{2,5}$ (cinquefoil) | I | $0.005$ |
| $pp \to ppn$ | 2 $\to$ 3 | $L_+$ (Hopf link) | II | $0.000$ |
| $ppn \to ppnn$ | 3 $\to$ 4 | $L_+$ | II | $0.000$ |
| $ppnn \to pppnn$ | 4 $\to$ 5 | $L_-$ (mirror Hopf) | II | $0.000$ |
| $pppnn \to pppnnn$ | 5 $\to$ 6 | $C_{pn}$ (bare crossing) | III | $0.000$ |

**Key observation:** the operator transitions from $T_{2,5}$
(torus knot) to $L_+$ (Hopf) at the first magic number ($Z = 2$),
then to $L_-$ (mirror Hopf) at the shell boundary, then to
$C_{pn}$ (bare crossing) in the open shell.  The
$\mathcal{B}_3$ Borromean operator is **never selected** at the
nuclear level — it is purely a quark-level confinement operator.

## Physical interpretation

- **Regime I** (torus knot): the first nucleons see each other as
  individual particles.  The collective effect is described by the
  cinquefoil $T_{2,5}$, the second-generation torus knot — this
  is the residual strong force between nucleons.

- **Regime II** (Hopf link): at magic numbers, the filled shell
  acts as a collective Hopf link.  The new nucleon crosses the
  entire shell, not individual nucleons.  This is the shell closure
  mechanism: the Hopf link binds the new nucleon to the collective
  shell.

- **Regime III** (bare crossing): beyond the magic shell, the
  nucleus is large enough that the new nucleon interacts via
  simple pairwise crossings.  The collective effects are
  already encoded in the existing NF.

## $\mathcal{B}_3$ is quark-level only

The Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$
confines three quarks into a nucleon
([confinement selection](#prop:confinement-operator-selection)).
At the nuclear level, the nucleon NF (a 6-component vector in
$H_3(q)$) is the input, and inter-nucleon binding uses a
different family of operators.  The three regimes above exhaust
the nuclear binding operators; $\mathcal{B}_3$ does not appear
among them.

**Witness**: `nuclear-binding-lp.witness.json`.
