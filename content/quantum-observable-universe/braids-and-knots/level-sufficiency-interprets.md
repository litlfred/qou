**Remark.**
*[Level sufficiency](#prop:level-sufficiency) is the formal
justification for a **default-coarse computational strategy**
across the full [confinement category](#def:confinement-category).
The hierarchy has at least four relevant levels:*

| *Level $\ell$* | *Confined particle* | *Default strand count $n_0$* |
|---|---|---|
| *0* | *quark* | *1* |
| *1* | *nucleon (proton, neutron)* | *3 (quark-strands)* |
| *2* | *atom / nucleus* | *$A$ (nucleon-strands)* |
| *3* | *compound / molecule* | *# atoms* |

*At each level, [prop:level-sufficiency](#prop:level-sufficiency)
implies that any trace-class invariant — mass $\mathfrak{m}(P)$,
binding $B(P)$, Jones polynomial $J_P(q)$ — is **exact**
at the coarsest representation satisfying
$k_{\max}(P, q, n_0) \le n_0$.*

**Default-coarse rule.**
*Every computational pipeline (mass, binding, stability, decay
channel, spectroscopy) should:*

1. *Identify the [confined particle](#def:confined-particle) $P$
   at its natural level $\ell$.*
2. *Read $k_{\max}(P, q, n_0)$ from the witness data
   ([confinement level](#def:confinement-level) paragraph
   "per-atom truncation").*
3. *If $k_{\max}(P, q, n_0) \le n_0$, compute $\mathrm{tr}_M$ at
   the coarse level and halt.*
4. *If $k_{\max}(P, q, n_0) > n_0$, apply the unfolding morphism
   $\uparrow_\ell$ in [confinement category](#def:confinement-category)
   and repeat at $\ell - 1$.*

**Unfolding triggers (two categories).**

- ***Magic shell closure.***  *Atoms at $A \in \{2, 8, 20, 28, 50,
  82, 126\}$ and noble-gas electron counts $Z \in \{2, 10, 18, 36,
  54, 86\}$ exhibit binding multiplicity $\mu(S, q) \ge 2$
  ([electron shell](#def:electron-shell)), forcing
  $k_{\max}$ above the coarse count.  Atoms in these rows must be
  computed one level deeper.*
- ***SDP cross-channel demand.***  *When the active dual support
  $\mathcal{S}^*$ of the [confinement SDP](#prop:confinement-sdp)
  spans blocks $\lambda_1, \lambda_2$ with
  $\max(|\lambda_1|, |\lambda_2|) > n_0$, the coarse representation
  cannot express the coupling and unfolding is required.*

*Non-magic atoms and molecules without SDP cross-channel demand are
computed at their natural coarse level — this is not an
approximation, it is the **minimal exact representation**.*

**Dressing preserves computational minimality.**
*Under the [dressing morphism](#def:dressed-particle)
$\mathrm{dress}_S: P_{\mathrm{bare}} \to P_{\mathrm{dressed}}$, the
witnessed truncation updates to*

$$
  k_{\max}(P_{\mathrm{dressed}}, q)
  \;=\;
  \max\bigl(k_{\max}(P_{\mathrm{bare}}, q),\;
            k_{\max}^{\mathrm{bind}}(S, q)\bigr),
$$

*where $k_{\max}^{\mathrm{bind}}$ is the partition reach of the
binding subword $W_{\mathrm{bind}}$.  The dressed particle's
computational level is then determined by
[prop:level-sufficiency](#prop:level-sufficiency) with the updated
$k_{\max}$ — adding a single electron to a non-magic atom typically
leaves the computational level unchanged, while closing to a noble
gas triggers $\mu \ge 2$ and raises the required level.*

**Computational implication.**
*For a non-magic atom with $A$ nucleons, the Hecke algebra
dimension drops from $|H_{3A}(q)| = (3A)!$ (quark-level) to
$|H_A(R, q)| = A!$ (nucleon-level).  Partition enumeration drops from
$p(3A)$ to $p(A)$: for $A = 20$, a factor of
$p(60)/p(20) \approx 966{,}000/627 \approx 1540$.
Default-coarse computation is not a performance heuristic — it is
the computational content of
[prop:level-sufficiency](#prop:level-sufficiency) applied via the
[confinement category](#def:confinement-category).*

**Earlier special case.**
*The remark
[nucleon-as-unit justification](#rem:confinement-nucleon-unit)
is the special case of this framework at the atom→nucleon
transition ($\ell = 2 \to \ell = 1$).
[Prop:level-sufficiency](#prop:level-sufficiency) generalises it
uniformly across the full hierarchy — quark to molecule — and for
any knot-operator content, including the multi-operator
$\mu(S, q) \ge 2$ regime introduced by
[electron shells](#def:electron-shell) and
[dressing](#def:dressed-particle).*
