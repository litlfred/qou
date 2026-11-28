//! Oriented binomial / lattice-kernel Gröbner & Graver vector peeling over $\mathbb{N}^m$
//! and functorial column promotion across conserved-charge strata.
//!
//! Given an integer stoichiometry or conserved-charge matrix $A \in \mathbb{Z}^{d \times m}$,
//! any kernel vector $g = u^+ - u^- \in \ker(A) \cap \mathbb{Z}^m$ defines a conservative
//! binomial move $u \mapsto u - u^- + u^+$ on non-negative integer occupancies $u \in \mathbb{N}^m$
//! preserving $A u$. Orienting a Conti–Traverso / Graver test set by a linear cost vector
//! $c \in K^m$ (with lexicographic tie-breaking on cost ties) yields terminating normal-form
//! reduction to fiber-optimal configurations, together with Dantzig–Wolfe reduced costs
//! $\bar{c}_j(y) = c_j - (A^\top y)_j$ and functorial column promotion $A_{\text{next}} = A\,M$.

use std::cmp::Ordering;
use std::collections::BTreeSet;

use num_integer::Integer;
use serde::{Deserialize, Serialize};

use crate::scalar::RingScalar;

/// Dense integer matrix $A \in \mathbb{Z}^{d \times m}$ representing conserved charges or
/// stoichiometric balances across $d$ rows and $m$ columns.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct IntegerMatrix {
    rows: usize,
    cols: usize,
    data: Vec<i64>,
}

impl IntegerMatrix {
    /// Construct a `rows x cols` matrix from row-major `data`.
    pub fn new(rows: usize, cols: usize, data: Vec<i64>) -> Self {
        assert_eq!(
            data.len(),
            rows * cols,
            "IntegerMatrix data length {} != {} * {}",
            data.len(),
            rows,
            cols
        );
        Self { rows, cols, data }
    }

    /// Number of rows $d$.
    pub fn rows(&self) -> usize {
        self.rows
    }

    /// Number of columns $m$.
    pub fn cols(&self) -> usize {
        self.cols
    }

    /// Entry $A_{r, c}$.
    pub fn get(&self, r: usize, c: usize) -> i64 {
        self.data[r * self.cols + c]
    }

    /// Matrix-vector product $A z \in \mathbb{Z}^d$ for $z \in \mathbb{Z}^m$.
    pub fn mul_vec_i64(&self, z: &[i64]) -> Vec<i64> {
        assert_eq!(z.len(), self.cols, "vector length mismatch");
        let mut out = vec![0i64; self.rows];
        for r in 0..self.rows {
            let mut sum = 0i64;
            for c in 0..self.cols {
                sum = sum
                    .checked_add(
                        self.get(r, c)
                            .checked_mul(z[c])
                            .expect("i64 mul overflow in IntegerMatrix::mul_vec_i64"),
                    )
                    .expect("i64 add overflow in IntegerMatrix::mul_vec_i64");
            }
            out[r] = sum;
        }
        out
    }

    /// Matrix-vector product $A u \in \mathbb{Z}^d$ for non-negative occupancy $u \in \mathbb{N}^m$.
    pub fn mul_vec_u64(&self, u: &[u64]) -> Vec<i64> {
        let z: Vec<i64> = u
            .iter()
            .map(|&x| i64::try_from(x).expect("u64 occupancy exceeds i64::MAX"))
            .collect();
        self.mul_vec_i64(&z)
    }

    /// Returns `true` iff $A z = 0$.
    pub fn is_in_kernel(&self, z: &[i64]) -> bool {
        self.mul_vec_i64(z).into_iter().all(|x| x == 0)
    }

    /// Matrix product $self \cdot rhs$ (`(d x m) * (m x p) -> (d x p)`), implementing functorial
    /// column promotion $A_{k+1} = A_k M_{k \to k+1}$.
    pub fn mul_mat(&self, rhs: &Self) -> Self {
        assert_eq!(
            self.cols, rhs.rows,
            "incompatible matrix dimensions {}x{} * {}x{}",
            self.rows, self.cols, rhs.rows, rhs.cols
        );
        let mut out = vec![0i64; self.rows * rhs.cols];
        for r in 0..self.rows {
            for c in 0..rhs.cols {
                let mut sum = 0i64;
                for k in 0..self.cols {
                    sum = sum
                        .checked_add(
                            self.get(r, k)
                                .checked_mul(rhs.get(k, c))
                                .expect("i64 mul overflow in mul_mat"),
                        )
                        .expect("i64 add overflow in mul_mat");
                }
                out[r * rhs.cols + c] = sum;
            }
        }
        Self {
            rows: self.rows,
            cols: rhs.cols,
            data: out,
        }
    }
}

/// Oriented binomial rewrite rule $u^- \longrightarrow u^+$ on $\mathbb{N}^m$ representing
/// the conservative step $u \mapsto u - u^- + u^+$ whenever $u \ge u^-$ componentwise.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct BinomialRule {
    /// Consumed reactant/source multiplicities $u^- \in \mathbb{N}^m$.
    pub u_minus: Vec<u64>,
    /// Produced product/target multiplicities $u^+ \in \mathbb{N}^m$.
    pub u_plus: Vec<u64>,
}

impl BinomialRule {
    /// Construct from explicit disjoint-support `u_minus -> u_plus` vectors of equal length.
    pub fn new(u_minus: Vec<u64>, u_plus: Vec<u64>) -> Self {
        assert_eq!(u_minus.len(), u_plus.len(), "u_minus/u_plus length mismatch");
        assert!(
            u_minus != u_plus,
            "trivial binomial u -> u would loop forever"
        );
        Self { u_minus, u_plus }
    }

    /// Construct directly from a non-zero signed vector $g = u^+ - u^- \in \mathbb{Z}^m$
    /// (`u_minus = max(-g, 0)`, `u_plus = max(g, 0)`).
    pub fn from_signed_move(g: &[i64]) -> Option<Self> {
        if g.iter().all(|&x| x == 0) {
            return None;
        }
        let mut u_minus = Vec::with_capacity(g.len());
        let mut u_plus = Vec::with_capacity(g.len());
        for &x in g {
            if x > 0 {
                u_plus.push(x as u64);
                u_minus.push(0);
            } else if x < 0 {
                u_plus.push(0);
                u_minus.push(x.unsigned_abs());
            } else {
                u_plus.push(0);
                u_minus.push(0);
            }
        }
        Some(Self { u_minus, u_plus })
    }

    /// Orient a kernel vector $g \in \mathbb{Z}^m \setminus \{0\}$ so the step strictly decreases
    /// linear objective $\sum_j c_j u_j$ (breaking exact cost ties by lexicographic decrease
    /// $u^- >_{\text{lex}} u^+$ to guarantee termination).
    pub fn orient_by_cost<K: RingScalar + Ord>(g: &[i64], costs: &[K]) -> Option<Self> {
        assert_eq!(g.len(), costs.len(), "move/cost length mismatch");
        if g.iter().all(|&x| x == 0) {
            return None;
        }
        let delta = linear_cost(costs, g);
        match delta.cmp(&K::zero()) {
            Ordering::Less => Self::from_signed_move(g),
            Ordering::Greater => {
                let neg_g: Vec<i64> = g.iter().map(|&x| -x).collect();
                Self::from_signed_move(&neg_g)
            }
            Ordering::Equal => {
                let fwd = Self::from_signed_move(g)?;
                if fwd.u_minus > fwd.u_plus {
                    Some(fwd)
                } else {
                    Some(Self {
                        u_minus: fwd.u_plus,
                        u_plus: fwd.u_minus,
                    })
                }
            }
        }
    }

    /// Net signed change $g = u^+ - u^- \in \mathbb{Z}^m$.
    pub fn net_move(&self) -> Vec<i64> {
        self.u_plus
            .iter()
            .zip(self.u_minus.iter())
            .map(|(&p, &m)| (p as i64) - (m as i64))
            .collect()
    }

    /// Returns `true` iff $u_j \ge u^-_j$ for every coordinate $j$.
    pub fn is_applicable(&self, u: &[u64]) -> bool {
        u.len() == self.u_minus.len() && u.iter().zip(&self.u_minus).all(|(&uj, &mj)| uj >= mj)
    }

    /// Apply $u \mapsto u - u^- + u^+$ if applicable.
    pub fn apply(&self, u: &[u64]) -> Option<Vec<u64>> {
        if !self.is_applicable(u) {
            return None;
        }
        Some(
            u.iter()
                .zip(&self.u_minus)
                .zip(&self.u_plus)
                .map(|((&uj, &mj), &pj)| uj - mj + pj)
                .collect(),
        )
    }
}

/// Evaluate linear cost $\sum_{j=0}^{m-1} z_j c_j \in K$.
pub fn linear_cost<K: RingScalar>(costs: &[K], z: &[i64]) -> K {
    assert_eq!(costs.len(), z.len(), "cost/vector length mismatch");
    let mut acc = K::zero();
    for (c, &zj) in costs.iter().zip(z.iter()) {
        if zj != 0 && !c.is_zero() {
            acc = acc.add_val(&K::from_i64(zj).mul_val(c));
        }
    }
    acc
}

/// Evaluate LP reduced costs $\bar{c}_j(y) = c_j - \sum_{i=0}^{d-1} A_{i,j} y_i$ for all columns $j$.
pub fn reduced_costs<K: RingScalar>(
    charge_matrix: &IntegerMatrix,
    costs: &[K],
    dual_y: &[K],
) -> Vec<K> {
    assert_eq!(costs.len(), charge_matrix.cols());
    assert_eq!(dual_y.len(), charge_matrix.rows());
    let mut out = Vec::with_capacity(charge_matrix.cols());
    for j in 0..charge_matrix.cols() {
        let mut shadow = K::zero();
        for (i, yi) in dual_y.iter().enumerate() {
            let a_ij = charge_matrix.get(i, j);
            if a_ij != 0 && !yi.is_zero() {
                shadow = shadow.add_val(&K::from_i64(a_ij).mul_val(yi));
            }
        }
        out.push(costs[j].sub_val(&shadow));
    }
    out
}

/// Functorial column promotion $A_{\text{next}} = A_{\text{curr}} \cdot M$ together with
/// induced composite column costs $c_{\text{next}, k} = \sum_j M_{j, k} c_{\text{curr}, j}$.
pub fn promote_stratum_columns<K: RingScalar>(
    a_curr: &IntegerMatrix,
    m_curr_to_next: &IntegerMatrix,
    costs_curr: &[K],
) -> (IntegerMatrix, Vec<K>) {
    assert_eq!(costs_curr.len(), a_curr.cols());
    let a_next = a_curr.mul_mat(m_curr_to_next);
    let mut costs_next = Vec::with_capacity(m_curr_to_next.cols());
    for col in 0..m_curr_to_next.cols() {
        let mut sum = K::zero();
        for row in 0..m_curr_to_next.rows() {
            let m_val = m_curr_to_next.get(row, col);
            if m_val != 0 {
                sum = sum.add_val(&K::from_i64(m_val).mul_val(&costs_curr[row]));
            }
        }
        costs_next.push(sum);
    }
    (a_next, costs_next)
}

fn vec_gcd(v: &[i64]) -> i64 {
    let mut g = 0i64;
    for &x in v {
        g = g.gcd(&x.abs());
    }
    g
}

fn conformal_le(u: &[i64], v: &[i64]) -> bool {
    u.iter()
        .zip(v.iter())
        .all(|(&uj, &vj)| (uj as i128) * (vj as i128) >= 0 && uj.abs() <= vj.abs())
}

/// Compute the symmetric Graver basis $\mathcal{G}(A) \subset \ker(A) \setminus \{0\}$ from a
/// lattice basis of $\ker_{\mathbb{Z}}(A)$ via Pottier's conformal S-vector algorithm, returning
/// one canonical sign representative (first non-zero entry $> 0$) per $\{\pm g\}$ pair.
pub fn pottier_graver_basis(kernel_basis: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let mut g_set: BTreeSet<Vec<i64>> = BTreeSet::new();
    for b in kernel_basis {
        let d = vec_gcd(b);
        if d > 0 {
            let prim: Vec<i64> = b.iter().map(|&x| x / d).collect();
            let neg: Vec<i64> = prim.iter().map(|&x| -x).collect();
            g_set.insert(prim);
            g_set.insert(neg);
        }
    }

    loop {
        let mut cur: Vec<Vec<i64>> = g_set.iter().cloned().collect();
        cur.sort_by_key(|v| (v.iter().map(|x| x.abs()).sum::<i64>(), v.clone()));
        let mut added: BTreeSet<Vec<i64>> = BTreeSet::new();

        for i in 0..cur.len() {
            for j in (i + 1)..cur.len() {
                let u = &cur[i];
                let w = &cur[j];
                if !u
                    .iter()
                    .zip(w.iter())
                    .any(|(&uj, &wj)| (uj as i128) * (wj as i128) < 0)
                {
                    continue;
                }
                let mut s: Vec<i64> = u.iter().zip(w.iter()).map(|(&a, &b)| a + b).collect();
                if s.iter().all(|&x| x == 0) {
                    continue;
                }
                let mut reduced = true;
                while reduced {
                    reduced = false;
                    for g in &cur {
                        if g != &s && conformal_le(g, &s) {
                            for (sj, &gj) in s.iter_mut().zip(g.iter()) {
                                *sj -= gj;
                            }
                            reduced = true;
                            break;
                        }
                    }
                }
                if s.iter().any(|&x| x != 0) && !g_set.contains(&s) && !added.contains(&s) {
                    let neg_s: Vec<i64> = s.iter().map(|&x| -x).collect();
                    added.insert(s);
                    added.insert(neg_s);
                }
            }
        }

        if added.is_empty() {
            break;
        }
        g_set.extend(added);
        // Prune conformally non-minimal elements:
        let all: Vec<Vec<i64>> = g_set.iter().cloned().collect();
        let mut minimal = BTreeSet::new();
        for v in &all {
            if !all.iter().any(|u| u != v && conformal_le(u, v)) {
                minimal.insert(v.clone());
            }
        }
        g_set = minimal;
    }

    // Return unique canonical sign representatives (first non-zero entry > 0):
    let mut pos_reps = BTreeSet::new();
    for v in g_set {
        if let Some(&first_nz) = v.iter().find(|&&x| x != 0) {
            if first_nz > 0 {
                pos_reps.insert(v);
            }
        }
    }
    pos_reps.into_iter().collect()
}

/// Oriented binomial rewriting basis over $\mathbb{N}^m$ preserving $A u = b$.
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
pub struct BinomialBasis {
    charge_matrix: IntegerMatrix,
    rules: Vec<BinomialRule>,
}

impl BinomialBasis {
    /// Construct from an `IntegerMatrix` and explicit `BinomialRule`s, verifying every rule
    /// conserves $A(u^+ - u^-) = 0$.
    pub fn try_new(
        charge_matrix: IntegerMatrix,
        rules: Vec<BinomialRule>,
    ) -> Result<Self, &'static str> {
        for r in &rules {
            if r.u_minus.len() != charge_matrix.cols() {
                return Err("binomial rule dimension does not match matrix columns");
            }
            if !charge_matrix.is_in_kernel(&r.net_move()) {
                return Err("binomial rule does not conserve A * (u^+ - u^-) = 0");
            }
        }
        Ok(Self {
            charge_matrix,
            rules,
        })
    }

    /// Build a universal oriented Conti–Traverso / Graver binomial Gröbner basis from a lattice
    /// basis of $\ker_{\mathbb{Z}}(A)$ and column cost vector `costs`.
    pub fn from_kernel_and_costs<K: RingScalar + Ord>(
        charge_matrix: IntegerMatrix,
        kernel_basis: &[Vec<i64>],
        costs: &[K],
    ) -> Result<Self, &'static str> {
        for kvec in kernel_basis {
            if kvec.len() != charge_matrix.cols() || !charge_matrix.is_in_kernel(kvec) {
                return Err("kernel basis vector is not in ker(A)");
            }
        }
        let graver = pottier_graver_basis(kernel_basis);
        let rules: Vec<BinomialRule> = graver
            .iter()
            .filter_map(|g| BinomialRule::orient_by_cost(g, costs))
            .collect();
        Self::try_new(charge_matrix, rules)
    }

    /// Underlying conserved-charge matrix $A$.
    pub fn charge_matrix(&self) -> &IntegerMatrix {
        &self.charge_matrix
    }

    /// Active oriented binomial rules.
    pub fn rules(&self) -> &[BinomialRule] {
        &self.rules
    }

    /// Reduce an initial occupancy vector $u \in \mathbb{N}^m$ modulo the oriented binomial basis,
    /// returning `(u_normal_form, rewrite_steps_applied)`.
    pub fn reduce_occupancy(&self, u: &[u64]) -> (Vec<u64>, usize) {
        assert_eq!(u.len(), self.charge_matrix.cols());
        let mut cur = u.to_vec();
        let mut steps = 0usize;
        loop {
            let mut stepped = false;
            for rule in &self.rules {
                if let Some(next) = rule.apply(&cur) {
                    cur = next;
                    steps += 1;
                    stepped = true;
                    break;
                }
            }
            if !stepped {
                break;
            }
        }
        (cur, steps)
    }

    /// Identify column indices with strictly negative reduced cost $\bar{c}_j(y) < 0$ (Dantzig–Wolfe
    /// column promotion candidates).
    pub fn negative_reduced_cost_columns<K: RingScalar + Ord>(
        &self,
        costs: &[K],
        dual_y: &[K],
    ) -> Vec<usize> {
        reduced_costs(&self.charge_matrix, costs, dual_y)
            .into_iter()
            .enumerate()
            .filter_map(|(j, rc)| if rc < K::zero() { Some(j) } else { None })
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn cho_stoichiometry_graver_peeling_and_stratum_promotion() {
        // 3 x 7 C-H-O elemental conservation matrix for species (C, H2, O2, CO, CO2, H2O, CH4):
        // C : [1, 0, 0, 1, 1, 0, 1]
        // H : [0, 2, 0, 0, 0, 2, 4]
        // O : [0, 0, 2, 1, 2, 1, 0]
        let a_cho = IntegerMatrix::new(
            3,
            7,
            vec![
                1, 0, 0, 1, 1, 0, 1, // C
                0, 2, 0, 0, 0, 2, 4, // H
                0, 0, 2, 1, 2, 1, 0, // O
            ],
        );

        // Exact Z-basis of ker_Z(A_CHO) (free coordinates v_CO, v_CO2, v_H2O, v_CH4 with v_CO + v_H2O even):
        // b1: [ 0,  1,  0, -1,  1, -1,  0] (CO + H2O -> CO2 + H2)
        // b2: [ 1,  0,  0, -2,  1,  0,  0] (2 CO -> C + CO2)
        // b3: [ 0, -3,  0, -1,  0,  1,  1] (CO + 3 H2 -> CH4 + H2O)
        // b4: [-1,  0, -1,  0,  1,  0,  0] (C + O2 -> CO2)
        let z_basis = vec![
            vec![0, 1, 0, -1, 1, -1, 0],
            vec![1, 0, 0, -2, 1, 0, 0],
            vec![0, -3, 0, -1, 0, 1, 1],
            vec![-1, 0, -1, 0, 1, 0, 0],
        ];

        // Cross-check Pottier Graver basis against independent exhaustive [-6, 6]^4 kernel box scan:
        let graver_pottier = pottier_graver_basis(&z_basis);
        let mut ker_box: Vec<Vec<i64>> = Vec::new();
        for v_co in -6i64..=6 {
            for v_co2 in -6i64..=6 {
                for v_h2o in -6i64..=6 {
                    if (v_co + v_h2o).rem_euclid(2) != 0 {
                        continue;
                    }
                    let v_o2 = -(v_co + 2 * v_co2 + v_h2o) / 2;
                    for v_ch4 in -6i64..=6 {
                        let v_c = -(v_co + v_co2 + v_ch4);
                        let v_h2 = -(v_h2o + 2 * v_ch4);
                        let vec = vec![v_c, v_h2, v_o2, v_co, v_co2, v_h2o, v_ch4];
                        if vec.iter().any(|&x| x != 0) {
                            ker_box.push(vec);
                        }
                    }
                }
            }
        }
        ker_box.sort_by_key(|v| v.iter().map(|x| x.abs()).sum::<i64>());
        let mut minimal_box: Vec<Vec<i64>> = Vec::new();
        for v in &ker_box {
            if !minimal_box.iter().any(|u| conformal_le(u, v)) {
                minimal_box.push(v.clone());
            }
        }
        let mut box_pos_reps: BTreeSet<Vec<i64>> = BTreeSet::new();
        for v in minimal_box {
            if let Some(&nz) = v.iter().find(|&&x| x != 0) {
                if nz > 0 {
                    box_pos_reps.insert(v);
                }
            }
        }
        let expected_graver: Vec<Vec<i64>> = box_pos_reps.into_iter().collect();
        assert_eq!(graver_pottier, expected_graver);

        // Standard enthalpy-like integer formation costs (kJ/mol rounded: 0, 0, 0, -111, -394, -242, -75):
        let costs: Vec<i64> = vec![0, 0, 0, -111, -394, -242, -75];
        let basis = BinomialBasis::from_kernel_and_costs(a_cho.clone(), &z_basis, &costs).unwrap();
        assert_eq!(basis.rules().len(), expected_graver.len());

        // Initial inventory: 1 CH4 + 2 O2 (u = [0, 0, 2, 0, 0, 0, 1], b = (1, 4, 4)):
        // Exothermic combustion CH4 + 2 O2 -> CO2 + 2 H2O (cost -75 -> -394 + 2*(-242) = -878):
        let u_init = vec![0, 0, 2, 0, 0, 0, 1];
        let b_init = a_cho.mul_vec_u64(&u_init);
        assert_eq!(b_init, vec![1, 4, 4]);

        let (u_star, steps) = basis.reduce_occupancy(&u_init);
        assert!(steps >= 1);
        assert_eq!(a_cho.mul_vec_u64(&u_star), b_init);
        assert_eq!(u_star, vec![0, 0, 0, 0, 1, 2, 0]); // 1 CO2 + 2 H2O!

        // Verify reduced-cost fiber invariance under arbitrary shadow prices y = (-100, -50, -80):
        let y = vec![-100i64, -50, -80];
        let rc = reduced_costs(&a_cho, &costs, &y);
        let diff_vec: Vec<i64> = u_star
            .iter()
            .zip(&u_init)
            .map(|(&a, &b)| (a as i64) - (b as i64))
            .collect();
        assert_eq!(linear_cost(&costs, &diff_vec), linear_cost(&rc, &diff_vec));

        // Functorial stratum promotion A_next = A_cho * M (promoting CO2 and H2O columns):
        let m_prom = IntegerMatrix::new(
            7,
            2,
            vec![
                0, 0, // C
                0, 0, // H2
                0, 0, // O2
                0, 0, // CO
                1, 0, // CO2
                0, 1, // H2O
                0, 0, // CH4
            ],
        );
        let (a_next, c_next) = promote_stratum_columns(&a_cho, &m_prom, &costs);
        assert_eq!(a_next.mul_vec_u64(&[1, 2]), vec![1, 4, 4]);
        assert_eq!(c_next, vec![-394, -242]);
    }
}
