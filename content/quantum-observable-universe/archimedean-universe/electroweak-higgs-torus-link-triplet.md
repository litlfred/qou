**Conjecture (electroweak/Higgs torus-link triplet).**
*The standard-model electroweak gauge bosons $W^\pm, Z$ and the
Higgs scalar $H$ are identified, in any QOU built on
([Bring's surface](#def:brings-surface)) with EM/strong sector
$\{T_{2,9}, T_{3,5}\}$
([force-carrier Bring uniqueness](#prop:force-carrier-bring-uniqueness)),
with the **Bring-internal even-twist 2-component torus-link
triplet***

$$
  W^{\pm} \;\longleftrightarrow\; T(2,4),
  \qquad
  Z \;\longleftrightarrow\; T(2,6),
  \qquad
  H \;\longleftrightarrow\; T(2,8).
$$

*Each link has braid presentation $\sigma_1^{2k}$ in $B_2$ for
$k = 2, 3, 4$ respectively; their Seifert-surface genera are
$1, 2, 3$ — all $\leq 4$, hence all embed in the genus-$4$
Seifert fiber of Bring's surface alongside the saturating
force-carriers $\{T_{2,9}, T_{3,5}\}$ (genus $4$). All five
EM + EW carriers therefore live in the **same host** by
([prop:torus-embeddable-complete](#prop:torus-embeddable-complete));
no separate non-Bring host surfaces are required.*

**Where this conjecture comes from.**

A research-grade audit of the framework's torus-knot inventory
([NV-1 / FROB-FILTER conjectures, 2026-05-02](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-02-nv-frob-filter-conjectures.md))
established that:

1. **Bring's genus-$4$ capacity is saturated** by
   $\{T_{2,9}, T_{3,5}\}$ — the only two coprime solutions of
   $(p-1)(q-1) = 8$. No additional torus knots can embed at
   genus $\leq 4$ on Bring as saturating generators.
2. The weak-scale crossing count $N_v$ in the Fermi-constant
   decomposition $G_F = 1/(\sqrt{2}v^2)$, $v = N_v\,E_\times\,\mu_0$
   currently has no categorical derivation; closing this gap (the
   **NV-1** audit flag) requires identifying $W^\pm, Z$ as specific
   knots/links.
3. An exploratory SDP-feasibility probe
   ([`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/ew-higgs-sdp-probe.witness.json))
   on three candidate identification paths returned a **clean PSD
   discrimination**: only the non-Bring even-twist torus-link
   triplet $\{T(2,4), T(2,6), T(2,8)\}$ produced
   positive-semidefinite Hecke certificates on every Wedderburn
   block. The two competing paths — $T_{3,5}$ as unified weak
   triplet (Bring-internal), and non-torus knots ($4_1$ for
   Higgs, $5_2$ for $Z$, $3_1$ for $W$) — all failed PSD on the
   standard $(2,1)$ representation.

**Even-twist parity argument.**

*The argument is stated over the categorical coefficient ring $R$
(typically $R = \mathbb{Z}[q, q^{-1}]$ or its localization $\mathbb{Q}(q)$),
with $q$ generic — i.e. $q$ is **not a root of unity** in $R$ (so
$H_n(q)$ is semisimple over $R$ by the standard Hecke-algebra
semisimplicity criterion). Note $q = 1$ IS a root of unity and is
**excluded**.*

The $T(2, 2k)$ braid is $\sigma_1^{2k} \in B_2$. The Hecke
algebra $H_2(q)$ over $R$ has Wedderburn decomposition $H_2(q)
\cong R \oplus R$ with the two block projectors sym + alt, and
$\sigma_1$ acts as $q$ on sym and $-q^{-1}$ on alt. Hence
$\sigma_1^{2k}$ has block eigenvalues

$$
  \mathrm{sym}\colon\; q^{2k} \in R^\times,
  \qquad
  \mathrm{alt}\colon\; (-q^{-1})^{2k} \;=\; q^{-2k} \in R^\times.
$$

Both eigenvalues are units in $R$ (no sign ambiguity from the
even power); $\sigma_1^{2k+1}$ (odd-twist) has alt eigenvalue
$-q^{-(2k+1)}$, which carries an irremovable sign relative to
sym.

**Positivity / PSD specialization.** When $R$ is specialized to
a real-closed field $F$ via $q \mapsto q^* \in F$ with $q^* > 1$
(in particular at $q^* = q_0 \approx 1.10998$), both even-twist
eigenvalues become strictly positive elements of $F$:
$(q^*)^{2k} > 0$ and $(q^*)^{-2k} > 0$. The odd-twist alt
eigenvalue becomes negative under any such specialization
($-(q^*)^{-(2k+1)} < 0$). So **even-twist is the unique parity**
at which a 2-component torus link supports a positive-definite
Frobenius form **in every real-closed-field specialization**.

This is the proposition `prop:even-twist-torus-link-psd-feasibility`
(below) that *is* a derivable proposition — it follows mechanically
from the Hecke relation. The conjecture sits at the next layer:
*which* even-twist links carry $W^\pm, Z, H$.

**Why genera 1, 2, 3 specifically.**

The genera of the 2-component torus links $T(2, 2k)$ form an
arithmetic progression $g(T(2, 2k)) = k - 1$ (Seifert genus of the
canonical Seifert surface). Bring's saturating force-carriers
$\{T_{2,9}, T_{3,5}\}$ occupy genus $4$ (the maximum allowed). The
**Bring-internal complement** at lower genera $\{1, 2, 3\}$ admits
exactly the 2-component torus-link identifications $T(2, 4),
T(2, 6), T(2, 8)$ — all embedded in the same genus-$4$ Seifert
fiber by ([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)),
which gives the embeddability bound $g(T_{m,n}) \leq g(\Sigma_4) = 4$.

The **mass ordering** of the standard model
$m_{W^\pm}\;{<}\;m_Z\;{<}\;m_H$
($80.4 \;{<}\; 91.2 \;{<}\; 125.3$ GeV in CODATA / PDG) maps
monotonically onto the crossing-number ordering $4 < 6 < 8$ — a
necessary but not sufficient consistency check.

**What the conjecture closes.**

If true, the conjecture supplies the missing categorical structure
for the **NV-1** audit flag (the weak-scale crossing count). With
$W^\pm, Z, H$ identified as $T(2,4), T(2,6), T(2,8)$, the parallel
of the $1/\alpha_{EM}$ derivation
([`rem:alpha-em-categorical-trace`](#rem:alpha-em-categorical-trace))
becomes available for $G_F$:

See [Table 1](#tbl:electroweak-higgs-torus-link-triplet-table1-data).

Closing the open rows above is the explicit research program
unlocked by this conjecture.

**Status.** Open. The PSD-feasibility evidence is **necessary but
not sufficient** for uniqueness. PSD-feasibility holds for *every*
even-twist $T(2, 2k)$ at any $k \geq 1$ (proposition below), so the
SDP probe alone cannot select the specific triplet $\{T(2,4), T(2,6),
T(2,8)\}$ from the infinite family. **Full uniqueness factorises
into five sub-arguments**, only some of which are derivable
from the existing framework:

See [Table 2](#tbl:electroweak-higgs-torus-link-triplet-table2-data).

The conjecture as stated **rides on U2 + U4**. Closing each:

- **U2** would be discharged by a content block characterising
  *force-carrier* objects categorically (e.g., as morphisms in
  $\mathbf{C}$ rather than objects, or as elements of $\mathrm{End}_R$
  rather than $\mathrm{Hom}(\mathbf{1}, A)$). The matter-vs-force
  distinction is implicit in the existing framework but not codified
  as a proposition.
- **U4** would be discharged by a representation-theoretic
  proposition counting the EW mass eigenstates: the broken
  $\mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ has $3 + 1 = 4$ gauge
  generators, the Higgs mechanism eats $3$ Goldstones via the
  longitudinal modes of $W^\pm, Z$, leaving $4 - 3 = 1$ scalar plus
  $3$ massive vectors with $W^\pm$ mass-degenerate, hence $3$
  distinct masses. This is standard EW theory, but to enter the
  QOU framework as a derivable proposition it must be cast in
  $\mathbf{C}$ as a count of irreducible Wedderburn channels
  surviving the Higgs idempotent.

**Uniqueness analysis at $q_0$ (probe table for $T(2, 2k)$,
$k = 1..7$):**

See [Table 3](#tbl:electroweak-higgs-torus-link-triplet-table3-data).

*Every* row PSD-passes. The selection of rows 2–4 over rows 1, 5, 6, 7
comes from U2–U5, **not** from PSD.

**To promote to a `proposition`, one path:**

1. Author the open content blocks for U2 and U4 (currently
   structural premises).
2. Provide a PSLQ uniqueness witness at $\geq 1000$-dps confirming
   that $N_v$ has a unique short closed form in
   $\{q^k, [k]_q, \hbar_q^k\}$ when the $T(2, 4), T(2, 6), T(2, 8)$
   basis is added.

Together these would discharge the conjecture into a derivable
proposition. Until both are available, the identification is
*structurally consistent* but not *categorically unique*.

**Witness.**
[`ew-higgs-sdp-probe.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/ew-higgs-sdp-probe.witness.json)
— PSD-feasibility certificates for the three candidate paths
(α non-Bring even-twist; β $T_{3,5}$ double-duty; γ non-torus
knots). Path α passes every block; β and γ fail the standard
$(2,1)$ block.

---

**Proposition (even-twist 2-component torus links are
PSD-feasible).**
*Over the categorical ring $R$ with $q$ generic (not a root of
unity in $R$), and for every $k \geq 1$, the braid $\sigma_1^{2k}
\in B_2$ acts on the Hecke algebra $H_2(q)$ with Wedderburn-block
eigenvalues*

$$
  \mathrm{sym\text{-}eigenvalue}(\sigma_1^{2k}) = q^{2k},
  \qquad
  \mathrm{alt\text{-}eigenvalue}(\sigma_1^{2k}) = q^{-2k}
$$

*— both elements of $R^\times$ obtained from each other by the
bar involution $\iota \colon q \mapsto q^{-1}$. For every $k \geq
0$, $\sigma_1^{2k+1}$ has $\mathrm{alt\text{-}eigenvalue} =
-q^{-(2k+1)}$, carrying an irremovable sign relative to sym.*

*Under any specialization of $R$ to a real-closed field $F$ via
$q \mapsto q^* \in F$ with $q^* > 1$ (in particular at $q^* =
q_0$), the even-twist eigenvalues are both strictly positive in
$F$, so $\sigma_1^{2k}$ is **PSD-feasible**; the odd-twist
$\sigma_1^{2k+1}$ has a negative alt eigenvalue and is **never**
PSD-feasible under any such specialization.*

*Proof.* Direct from the Hecke relation
$(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ specialised to $i = 1$ in
$B_2$: $\sigma_1 = q$ on sym, $\sigma_1 = -q^{-1}$ on alt
([Hecke-Skein convention](#prop:hecke-skein-convention) §7a of
CLAUDE.md). Composition with itself $2k$ times preserves the sign
on sym and squares the sign on alt, giving $(-q^{-1})^{2k} =
q^{-2k}$. Odd powers retain the negative sign on alt. The
positivity statement under specialization $R \to F$ uses only
that $(q^*)^{2k} > 0$ for $q^* > 1$ in $F$, and the same for the
inverse power. $\square$

This proposition is the **even-twist parity selection rule**.
Together with the structural input that force-carrier links are
2-component torus links of $H_1(\Sigma_{\text{host}}, \mathbb{Z})$,
it *forces* the parity to be even.

**Remark (categorical origin via bar self-duality).** *The
even-twist parity rule is the topological face of the substrate's
**bar self-duality** ([bar-self-dual confinement band](#prop:bar-self-dual-confinement-band),
[bar T-duality of the substrate](#prop:bar-t-duality-substrate)).
Under the bar involution $\iota \colon q \mapsto q^{-1}$, the
sym and alt Hecke eigenvalues swap (up to sign):*
$\iota(\sigma_i|_{\rm sym}) = \iota(q) = q^{-1}$,
$\iota(\sigma_i|_{\rm alt}) = \iota(-q^{-1}) = -q$.
*An even-twist link $T(2, 2k)$ has braid $\sigma_1^{2k}$ with
eigenvalues $(q^{2k}, q^{-2k})$ — a $\iota$-conjugate pair, so
the link is $\iota$-self-dual at the eigenvalue level. Odd-twist
links $T(2, 2k+1)$ have eigenvalues $(q^{2k+1}, -q^{-(2k+1)})$
which differ in sign under $\iota$, breaking the self-duality.
Hence the parity selection rule is equivalent to "force-carrier
links must be bar-self-dual" — connecting U1 to the substrate's
$\mathbb{Z}/2 \times \mathbb{Z}/2$ duality structure on the
Descartes-family moduli.*
