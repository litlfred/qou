For light atoms on the **doubly-symmetric line $Z = N = k$**, the
canonical Kashaev binding-energy law

$$
  B_{\rm Kashaev} \;=\; \rho_{\rm struct} \cdot m_e \cdot
  \mathrm{Vol}_{\rm hyp}(K_A)
$$

acquires a **substrate-q correction** at finite $q$ that we
conjecture takes the form

$$
  B(Z\!=\!N\!=\!k,\;q)
  \;=\;
  m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr),
  \qquad A = 2k.
$$

At $q = 1$: $[A]_q = A$, recovering the classical integer Kashaev
law.

### Empirical support

Numerical match at $q_0 = 1.10998…$ for the four atoms in the table
([per-atom δρ probe](../../../folio-assistant/computations/per-atom-rho-deviation.witness.json)):

| atom | err (Kashaev) | err (corrected) | improvement |
|------|--------------:|----------------:|------------:|
| ²H   | $+1.090\,\%$  | $+0.011\,\%$    | $\times 99$ |
| ⁴He  | $+5.867\,\%$  | $+0.057\,\%$    | $\times 103$ |
| ¹²C  | $+5.410\,\%$  | $+0.063\,\%$    | $\times 86$ |
| ¹⁶O  | $+5.301\,\%$  | $+0.152\,\%$    | $\times 35$ |

¹²C and ¹⁶O close *via propagation* through the existing α-cluster
formula: their predicted binding energies are derived from
$B(\!^4\!\mathrm{He})$ as
$B(\!^{4n}\!\mathrm{X}) = n \cdot B(\!^4\!\mathrm{He}) + \binom{n}{2} \cdot c_{\alpha\alpha}$;
once $B(\!^4\!\mathrm{He})$ closes, the doubly-magic α-cluster chain
follows without re-fitting.

### Categorical interpretation

The dimensional anomaly $A - [A]_q$ identifies as the deficit of the
**q-dimension of the natural representation**
$V^{(A-1)} = \mathrm{Sym}^{A-1}(V)$ of $U_q(\mathfrak{sl}_2)$:

$$
  A - [A]_q
  \;=\;
  \dim_\mathbb{C} V^{(A-1)} \;-\; q\text{-dim}_q V^{(A-1)}.
$$

At $q > 1$ the q-dimension exceeds the integer dimension, so the
correction has sign $-([A]_q - A) < 0$: the integer Kashaev law
**overestimates** the binding by exactly the dimensional anomaly,
scaled by $m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A)$.

### Why Z=N specifically

The Z=N line has a Z↔N exchange symmetry of the substrate fluid
that the formula respects. For $Z \neq N$ atoms (³H, ³He), the
formula fails: ³H and ³He have q-corrections differing by $2.9\,\%$,
ruling out any Z↔N exchange-symmetric closed form and pointing to
a **Coulomb-asymmetry** correction
(cf. [Coulomb-q-Hecke audit](../../../docs/audits/2026-05-02-coulomb-q-hecke-principled.md))
that the substrate alone cannot absorb.

### Status

This conjecture is an **empirical regularity** at the $10^{-3}$
precision level — falsifiable by any single Z=N atom whose binding
deviates from the formula by more than $10^{-3}$. The natural
falsification target is **²⁰Ne** ($n_\alpha = 5$) once its native
non-α-cluster knot pairing is identified.

A categorical derivation requires three lemmas:

1. **L-1** (total-host-count): the Kashaev coefficient at finite $q$
   is intrinsically $\rho_{\rm struct} + A - [A]_q$, with the
   integer $\rho_{\rm struct}$ as its $q\to 1$ limit. **Open** — see
   the [identification of $[A]_q$ as a Markov trace audit](../../../docs/audits/2026-05-03-l1-A-q-as-markov-trace.md).
2. **L-2** (selective q-deformation): the Wedderburn-block
   multiplicity $\rho_{\rm struct}$ is q-independent on the generic
   locus. **Essentially classical** — see the [L-2 proof sketch](../../../docs/audits/2026-05-03-l2-selective-q-deformation-proof.md).
3. **L-3** (Z=N decoupling): the isospin-asymmetry correction
   $\delta_{\rm asym}(Z, N)$ vanishes at $Z = N$. Should follow from
   the Z↔N substrate symmetry; **tractable**.

This block is the **conjectural form**; downstream theorems consume
it via the Lean class
[`QOU.BraidKnot.ZeqNRhoCorrection`](z-eq-n-rho-correction.lean) per
the conditional-class policy of
[CLAUDE.md §3b](../../../CLAUDE.md).
