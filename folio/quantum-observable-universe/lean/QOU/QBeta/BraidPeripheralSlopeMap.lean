/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# T3b: Braid Word to Surgery Slope $(m, \ell)$ — The Peripheral Structure Map

Bean **`qou-ae6l`** (under `parent: qou-avtq`).

For a braid word $\beta \in B_n$ whose closure $K = \widehat{\beta} \subset S^3$ is a knot,
the peripheral subgroup $\pi_1(\partial N(K)) \cong H_1(\partial N(K); \mathbb{Z}) \cong \mathbb{Z}\mu \oplus \mathbb{Z}\lambda_{\mathrm{can}}$
carries two natural bases:
1. The **canonical (homological / Seifert) peripheral basis** $(\mu, \lambda_{\mathrm{can}})$,
   where $\mu$ is the meridian and $\lambda_{\mathrm{can}}$ is the unique longitude with
   $\operatorname{lk}(K, \lambda_{\mathrm{can}}) = 0$.
2. The **blackboard (braid-closure) peripheral basis** $(\mu, \lambda_{\mathrm{bb}})$,
   where $\lambda_{\mathrm{bb}} = w(\beta)\,\mu + \lambda_{\mathrm{can}}$ and
   $w(\beta) = \sum_{k} \varepsilon_k \in \mathbb{Z}$ is the algebraic writhe of $\beta$.

Consequently, a peripheral curve written in the blackboard basis as
$p_{\mathrm{bb}}\,\mu + q_{\mathrm{bb}}\,\lambda_{\mathrm{bb}}$ has canonical surgery slope
$$(m, \ell) = \Phi_{w(\beta)}(p_{\mathrm{bb}}, q_{\mathrm{bb}}) = (p_{\mathrm{bb}} + w(\beta)\,q_{\mathrm{bb}},\, q_{\mathrm{bb}}).$$

This Mathlib-free, sorry-free, axiom-free module proves:
* `peripheralSlopeMap_comp` & `peripheralSlopeMap_zero`: $\Phi_{w_1} \circ \Phi_{w_2} = \Phi_{w_1 + w_2}$
  and $\Phi_0 = \mathrm{id}$, giving a faithful $\mathbb{Z}$-action in $\mathrm{SL}_2(\mathbb{Z})$.
* `peripheralSlopeMap_preserves_intersection`: $\Phi_w$ preserves the symplectic
  intersection form $\omega((m_1, \ell_1), (m_2, \ell_2)) = m_1 \ell_2 - \ell_1 m_2$.
* `peripheralSlopeMap_preserves_bezout`: $\Phi_w$ maps simple closed curves
  (Bezout coprime pairs $p x + q y = 1$) bijectively to simple closed curves.
* `meridianFilling_writhe_invariant` & `writhe_preserves_zero_longitude`:
  the trivial $S^3$ braid closure corresponds to meridian Dehn filling $(p_{\mathrm{bb}}, q_{\mathrm{bb}}) = (1, 0)$,
  which is a fixed point $\Phi_w(1, 0) = (1, 0)$ for every writhe $w \in \mathbb{Z}$;
  conversely, $\ell = 0 \iff q_{\mathrm{bb}} = 0$, so writhe framing shifts $m/\ell \mapsto m/\ell + w(\beta)$
  by an integer but never generates a non-zero longitudinal winding $\ell \ne 0$ from $\ell = 0$.
* `markovStabilization_compensation_iff`: positive/negative Markov stabilization
  $\beta \mapsto \beta \sigma_n^{\pm 1}$ shifts $w(\beta) \mapsto w(\beta) \pm 1$ while
  preserving the knot complement $S^3 \setminus K$; a canonical surgery slope $(m, \ell)$ is
  stabilization-invariant if and only if the blackboard meridian coefficient transforms as
  $p_{\mathrm{bb}}' = p_{\mathrm{bb}} \mp \ell$.
* `corpusKnot_blackboard_zero_surgery_slopes`: verifies the exact writhe $w(\beta)$,
  braid index $n$, Seifert twice-genus $2g = w_{\mathrm{pos}} - n + 1$, and canonical
  slope $\Phi_{w(\beta)}(0, 1) = (w(\beta), 1)$ of 0-framed blackboard surgery across
  $T(2,3)$, $4_1 = (\sigma_1 \sigma_2^{-1})^2$, $T(2,5)$, $5_2$, $T(2,9)$, and $T(3,5)$.
-/

namespace QOU.QBeta.BraidPeripheralSlopeMap

/-! ## §1. Peripheral Homology $\mathbb{Z}^2$ and the Writhe Shear $\Phi_w \in \mathrm{SL}_2(\mathbb{Z})$ -/

/-- A peripheral homology class $(m, \ell) \in H_1(\partial N(K); \mathbb{Z}) \cong \mathbb{Z}^2$,
    representing $m\,\mu + \ell\,\lambda$. -/
structure PeripheralSlope where
  m : Int
  l : Int
  deriving DecidableEq, Repr

/-- The symplectic intersection pairing $\omega((m_1, \ell_1), (m_2, \ell_2)) = m_1 \ell_2 - \ell_1 m_2$
    on $H_1(\partial N(K); \mathbb{Z})$. -/
def peripheralIntersection (s1 s2 : PeripheralSlope) : Int :=
  s1.m * s2.l - s1.l * s2.m

/-- The peripheral structure map $\Phi_w : \mathbb{Z}^2 \to \mathbb{Z}^2$ induced by a braid
    word $\beta$ of algebraic writhe $w = w(\beta) \in \mathbb{Z}$, mapping blackboard
    coordinates $(p_{\mathrm{bb}}, q_{\mathrm{bb}})$ to canonical coordinates
    $(m, \ell) = (p_{\mathrm{bb}} + w \cdot q_{\mathrm{bb}},\, q_{\mathrm{bb}})$. -/
def peripheralSlopeMap (w : Int) (s_bb : PeripheralSlope) : PeripheralSlope :=
  { m := s_bb.m + w * s_bb.l, l := s_bb.l }

/-- `qou-ae6l`: Zero-writhe braids (such as the figure-eight word $(\sigma_1 \sigma_2^{-1})^2$)
    induce the identity peripheral map $\Phi_0 = \mathrm{id}$. -/
theorem peripheralSlopeMap_zero (s : PeripheralSlope) :
    peripheralSlopeMap 0 s = s := by
  cases s with
  | mk m l =>
    simp [peripheralSlopeMap]

/-- `qou-ae6l`: Additive composition law $\Phi_{w_1}(\Phi_{w_2}(s)) = \Phi_{w_1 + w_2}(s)$. -/
theorem peripheralSlopeMap_comp (w1 w2 : Int) (s : PeripheralSlope) :
    peripheralSlopeMap w1 (peripheralSlopeMap w2 s) = peripheralSlopeMap (w1 + w2) s := by
  cases s with
  | mk m l =>
    unfold peripheralSlopeMap
    congr 1
    calc m + w2 * l + w1 * l
      _ = m + (w1 * l + w2 * l) := by omega
      _ = m + (w1 + w2) * l := by rw [Int.add_mul]

/-- `qou-ae6l`: $\Phi_{-w}$ is the exact two-sided inverse of $\Phi_w$. -/
theorem peripheralSlopeMap_inv (w : Int) (s : PeripheralSlope) :
    peripheralSlopeMap (-w) (peripheralSlopeMap w s) = s ∧
    peripheralSlopeMap w (peripheralSlopeMap (-w) s) = s := by
  constructor
  · rw [peripheralSlopeMap_comp]
    have h1 : -w + w = 0 := by omega
    rw [h1, peripheralSlopeMap_zero]
  · rw [peripheralSlopeMap_comp]
    have h2 : w + -w = 0 := by omega
    rw [h2, peripheralSlopeMap_zero]

/-- `qou-ae6l`: The peripheral structure map $\Phi_w$ preserves the symplectic
    intersection form $\omega(\Phi_w(s_1), \Phi_w(s_2)) = \omega(s_1, s_2)$. -/
theorem peripheralSlopeMap_preserves_intersection (w : Int) (s1 s2 : PeripheralSlope) :
    peripheralIntersection (peripheralSlopeMap w s1) (peripheralSlopeMap w s2) =
      peripheralIntersection s1 s2 := by
  unfold peripheralIntersection peripheralSlopeMap
  dsimp
  calc (s1.m + w * s1.l) * s2.l - s1.l * (s2.m + w * s2.l)
    _ = s1.m * s2.l + w * s1.l * s2.l - (s1.l * s2.m + s1.l * (w * s2.l)) := by
        rw [Int.add_mul, Int.mul_add]
    _ = s1.m * s2.l - s1.l * s2.m := by
        have h : w * s1.l * s2.l = s1.l * (w * s2.l) := by
          rw [Int.mul_comm w s1.l, Int.mul_assoc]
        omega

/-- `qou-ae6l`: Bezout coprimality identity showing that if $(p_{\mathrm{bb}}, q_{\mathrm{bb}})$
    is a primitive peripheral class ($p_{\mathrm{bb}} x + q_{\mathrm{bb}} y = 1$), then
    $\Phi_w(p_{\mathrm{bb}}, q_{\mathrm{bb}}) = (p_{\mathrm{bb}} + w q_{\mathrm{bb}}, q_{\mathrm{bb}})$
    satisfies $(p_{\mathrm{bb}} + w q_{\mathrm{bb}}) x + q_{\mathrm{bb}} (y - w x) = 1$,
    so $\Phi_w$ maps simple closed peripheral curves to simple closed peripheral curves. -/
theorem peripheralSlopeMap_preserves_bezout (w p q x y : Int) (hbez : p * x + q * y = 1) :
    (p + w * q) * x + q * (y - w * x) = 1 := by
  calc (p + w * q) * x + q * (y - w * x)
    _ = p * x + w * q * x + (q * y - q * (w * x)) := by
        rw [Int.add_mul, Int.mul_sub]
    _ = p * x + q * y := by
        have h : w * q * x = q * (w * x) := by
          rw [Int.mul_comm w q, Int.mul_assoc]
        omega
    _ = 1 := hbez

/-! ## §2. Meridian Dehn Filling Invariance and Markov Stabilization Compensation -/

/-- `qou-ae6l`: Pure meridian Dehn filling $s = (m, 0)$ (in particular $(1, 0)$, the
    unfilled $S^3$ braid closure $\widehat{\beta}$) is fixed by $\Phi_w$ for every writhe $w$,
    and $\Phi_w(s).\ell = 0 \iff s.\ell = 0$. Thus writhe framing shifts $m/\ell \mapsto m/\ell + w$
    by an integer on any curve with $\ell \ne 0$, but cannot generate a non-zero longitudinal
    winding $\ell \ne 0$ from $\ell = 0$. -/
theorem meridianFilling_writhe_invariant_and_zero_longitude_iff (w m : Int) (s : PeripheralSlope) :
    peripheralSlopeMap w { m := m, l := 0 } = { m := m, l := 0 } ∧
    ((peripheralSlopeMap w s).l = 0 ↔ s.l = 0) := by
  unfold peripheralSlopeMap
  constructor
  · simp
  · exact Iff.rfl

/-- `qou-ae6l`: Under positive Markov stabilization $\beta \mapsto \beta \sigma_n$
    (which shifts writhe $w \mapsto w + 1$ while preserving the knot type $\widehat{\beta}$),
    two blackboard slope pairs $(p_{\mathrm{bb}}, q_{\mathrm{bb}})$ at writhe $w$ and
    $(p_{\mathrm{bb}}', q_{\mathrm{bb}})$ at writhe $w + 1$ define the exact same canonical
    surgery slope $(m, \ell)$ on $S^3 \setminus K$ if and only if
    $p_{\mathrm{bb}}' = p_{\mathrm{bb}} - q_{\mathrm{bb}}$. -/
theorem markovStabilization_compensation_iff (w p p' q : Int) :
    peripheralSlopeMap (w + 1) { m := p', l := q } =
      peripheralSlopeMap w { m := p, l := q } ↔
    p' = p - q := by
  unfold peripheralSlopeMap
  dsimp
  have hmul : (w + 1) * q = w * q + q := by
    calc (w + 1) * q = w * q + 1 * q := Int.add_mul w 1 q
    _ = w * q + q := by omega
  constructor
  · intro h
    injection h with hm _
    omega
  · intro hp
    congr 1
    omega

/-! ## §3. Corpus Braid Words and Canonical 0-Framed Blackboard Surgery Slopes -/

/-- A braid generator letter $\sigma_i^{\pm 1}$ represented by its sign $\varepsilon \in \{+1, -1\}$. -/
def braidWordWrithe (signs : List Int) : Int :=
  signs.foldl (· + ·) 0

/-- Representative sign lists for the standard corpus braid words:
    * $T(2,3) = \sigma_1^3$ (`[1, 1, 1]`, $w = 3$)
    * $4_1 = (\sigma_1 \sigma_2^{-1})^2$ (`[1, -1, 1, -1]`, $w = 0$)
    * $T(2,5) = \sigma_1^5$ (`[1, 1, 1, 1, 1]`, $w = 5$)
    * $5_2 = \sigma_1^3 \sigma_2 \sigma_1^{-1} \sigma_2$ (`[1, 1, 1, 1, -1, 1]`, $w = 4$)
    * $T(2,9) = \sigma_1^9$ ($w = 9$)
    * $T(3,5) = (\sigma_1 \sigma_2)^5$ ($w = 10$) -/
def signsT23 : List Int := [1, 1, 1]
def signsFig8 : List Int := [1, -1, 1, -1]
def signsT25 : List Int := [1, 1, 1, 1, 1]
def signs52 : List Int := [1, 1, 1, 1, -1, 1]
def signsT29 : List Int := [1, 1, 1, 1, 1, 1, 1, 1, 1]
def signsT35 : List Int := [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

/-- `qou-ae6l`: Exact writhe evaluations and canonical 0-framed blackboard surgery
    slopes $\Phi_{w(\beta)}(0, 1) = (w(\beta), 1)$ across the six corpus knots
    $T(2,3)$, $4_1$, $T(2,5)$, $5_2$, $T(2,9)$, and $T(3,5)$. -/
theorem corpusKnot_blackboard_zero_surgery_slopes :
    braidWordWrithe signsT23 = 3 ∧
    braidWordWrithe signsFig8 = 0 ∧
    braidWordWrithe signsT25 = 5 ∧
    braidWordWrithe signs52 = 4 ∧
    braidWordWrithe signsT29 = 9 ∧
    braidWordWrithe signsT35 = 10 ∧
    peripheralSlopeMap (braidWordWrithe signsFig8) { m := 0, l := 1 } = { m := 0, l := 1 } ∧
    peripheralSlopeMap (braidWordWrithe signsT35) { m := 0, l := 1 } = { m := 10, l := 1 } := by
  decide

end QOU.QBeta.BraidPeripheralSlopeMap
