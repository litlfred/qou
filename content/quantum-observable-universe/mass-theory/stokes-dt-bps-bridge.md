**Conjecture (closed-sector state-integral bridge — Vol-conjecture-style adoption).**
For a hyperbolic knot $K \subseteq S^3$, the resurgent Stokes constant of the
state integral of $S^3 \setminus K$ on its distinguished (geometric Borel) ray
is a **Donaldson--Thomas invariant / BPS degeneracy** of the associated
$3$d $\mathcal{N}=2$ theory $T[K]$:

$$
  \mathfrak{S}(K) \;=\; \Omega_{\mathrm{DT}}(K) \;=\; \dim \mathcal{H}_{\mathrm{BPS}}(T[K]),
$$

where $\mathfrak{S}(K)$ is the Stokes constant, $\Omega_{\mathrm{DT}}(K)$ the
Donaldson--Thomas / Kontsevich--Soibelman invariant of the $q$-difference
structure, and $\mathcal{H}_{\mathrm{BPS}}(T[K])$ the space of BPS states whose
graded dimension categorifies the $3$d index.

The first equality is
[`garoufalidis-gu-marino2023peacock`] Conjecture 3(d) — *"the Stokes
constants are integers corresponding to the Donaldson--Thomas invariants and the
BPS degeneracies"* — proved by Garoufalidis--Gu--Mariño for the figure-eight
$4_1$. The second is the [`gukov-pei-putrov-vafa2017`] (GPPV) realisation of the
DT/BPS count as the graded dimension of the fivebrane BPS Hilbert space of
$T[M_3]$ on $M_3 \times D^2$, categorifying the $3$d $\mathcal{N}=2$ indices; the
$3$d--$3$d dictionary is [`dimofte-gaiotto-gukov2013`] (DGG).

### Which BPS sector — the non-degeneracy result

Two published knot-homology/BPS bridges live in the literature, and they identify
**different** BPS spaces:

| Bridge | BPS sector | $4_1$ count |
|--------|-----------|-------------|
| Gukov--Stošić [`gukov-stosic2012`] | **open** BPS states (conormal $L_K \subset T^*S^3$; colored HOMFLY homology) | $\det(4_1) = 5$ |
| GPPV [`gukov-pei-putrov-vafa2017`] + GGM Conj 3(d) | **closed** / state-integral ($\hat{Z}$; resurgent Stokes) | $\{3, 4\}$ |

The **open**-HOMFLY count is fixed by the knots--quivers correspondence
[`kucharski-reineke-stosic-sulkowski2017`]: the quiver of a knot has one node per
HOMFLY-PT homology generator, so the $4_1$ open-BPS count is
$\det(4_1) = 5$ (calibrated by that paper's worked trefoil, $3 = \det 3_1$ nodes).
Since $5 \notin \{3, 4\}$, the **open**-HOMFLY Gukov--Stošić bridge does *not*
reproduce the GGM resurgent-Stokes spectrum $\{3, 4\}$ and does *not* license
$A_\omega = 3$. Only the **closed**-sector bridge stated above reproduces
$\{3, 4\}$ (reduced symmetry constant $3$); its $q \to 0$ anchor $S^+(0)_{01} = 3$
is machine-checked unconditionally (`QOU.QBeta.StokesQZeroDTCount`).

We therefore adopt the **closed**-sector bridge, and A_ω=3 is made
conditional on it downstream
([`thm:aomega-fourone-dt-count`](#thm:aomega-fourone-dt-count)) — a theorem for
$4_1$, conjectural in general. It is *not* the open-HOMFLY bridge.

### Lean axiomatisation

The bridge is a Lean typeclass `QOU.QBeta.StokesDTBPSBridge` carrying the two
identifications as fields:

```lean
class StokesDTBPSBridge (Knot : Type*) where
  stokesConstant : Knot → ℤ
  dtInvariant    : Knot → ℤ
  bpsDim         : Knot → ℤ
  stokes_eq_dt : ∀ K, stokesConstant K = dtInvariant K   -- GGM Conj 3(d)
  dt_eq_bps    : ∀ K, dtInvariant K   = bpsDim K          -- GPPV
```

The fields are the conjecture's *inputs*; no field asserts a value of $A_\omega$.
Any instance is the conjecture holding; none is supplied (the general statement is
open — it is a theorem for $4_1$). Downstream results take
`[StokesDTBPSBridge Knot]` as an explicit hypothesis and are then fully verified
by Lean modulo that class instance, following the same pattern as
[`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md).
