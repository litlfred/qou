//! Temperley–Lieb cable transfer engine — colored-Jones J'_N via the
//! Jones–Wenzl (N−1)-cable, **full-MPFR** precision.
//!
//! Independent sibling of `tl_cable` (the incumbent engine on main, whose
//! fast path `jp_f64` runs dense f64 with f64-grade control gates): this
//! module keeps EVERY arithmetic step at MPFR (`rug::Float`, precision a
//! parameter, default 192 bits), so the N=6 certification gates land at
//! ~1e-41 instead of ~1e-8. The two engines were written independently in
//! parallel sessions and agree at N=6 to all 12 displayed digits
//! (B₆(5₂;q*) = −99594.247…) — a two-route confirmation. Use `tl_cable`
//! (jp_f64) for fast scans; use this module when the certificate itself
//! must carry full precision.
//!
//! Rust port of the validated Python engine in
//! `computations/probes/qbeta_5two_n3_cable_arbitration_probe.py` (A5.2,
//! PR #3927) + `qbeta_5two_higher_cable_qstar_probe.py` (A5.3, PR #4032),
//! built for the N=6 rung where TL₁₅ (Catalan(15) = 9 694 845 diagrams)
//! is out of pure-Python reach. Semantics are kept identical to the
//! Python reference so cross-checks at N = 3, 4, 5 gate the port:
//!
//! * basis = noncrossing perfect matchings of 2n boundary points,
//!   labels 0..n−1 top (circular position = label) and n..2n−1 bottom
//!   (circular position of label a ≥ n is 3n−1−a);
//! * right-multiplication d·U_i with δ^{loops} bookkeeping (δ = −A²−A⁻²,
//!   A = q^{−1/2});
//! * braid generator σ_i = A·1 + A⁻¹·U_i (Kauffman), inverse swaps A↔A⁻¹;
//! * Markov closure valued δ^{loops−1};
//! * c-cable of a braid word: σ_i ↦ the c² block of adjacent
//!   transpositions (inverses reversed and negated);
//! * Jones–Wenzl e_m by the Wenzl recursion
//!   e_k = e_{k−1} − ([k−1]/[k])·e_{k−1}U_{k−1}e_{k−1}, with the
//!   δ-Chebyshev brackets [1]=1, [2]=δ, [k+1]=δ[k]−[k−1].
//!
//! The one algorithmic upgrade over the Python reference: e_m is
//! normalized into the **TL_m diagram basis** (Catalan(m) terms with
//! loop-free reduced words) instead of the raw Wenzl word expansion,
//! whose term count explodes as t_k = t_{k−1}² + t_{k−1} (42 at m=4 but
//! 1806 at m=5). Both representations are the same algebra element; the
//! JW self-tests (absorption U_i·e_m = 0, idempotence e_m² = e_m,
//! ⟨e_m⟩ = [m+1]) plus the N ≤ 5 value cross-checks gate the change.

use rayon::prelude::*;
use rug::ops::CompleteRound;
use rug::Float;
use rustc_hash::FxHashMap;

/// Catalan number (exact for n ≤ 30 in u64).
pub fn catalan(n: usize) -> u64 {
    let mut c: u64 = 1;
    for i in 0..n as u64 {
        c = c * 2 * (2 * i + 1) / (i + 2);
    }
    c
}

/// Circular position of a boundary label (top 0..n−1 L→R, then bottom
/// labels n..2n−1 sit at positions 2n−1..n, i.e. R→L below).
#[inline]
fn pos(label: usize, n: usize) -> usize {
    if label < n { label } else { 3 * n - 1 - label }
}

/// Inverse of `pos`: label at a circular position.
#[inline]
fn label_at(c: usize, n: usize) -> usize {
    if c < n { c } else { 3 * n - 1 - c }
}

/// Decode a Dyck mask (bit c set ⇔ circular position c is an opener)
/// into the partner array over labels (partner[a] = b ⇔ {a,b} paired).
pub fn decode(mask: u64, n: usize) -> Vec<u8> {
    let two_n = 2 * n;
    let mut partner = vec![0u8; two_n];
    let mut stack: Vec<usize> = Vec::with_capacity(n);
    for c in 0..two_n {
        if (mask >> c) & 1 == 1 {
            stack.push(c);
        } else {
            let o = stack.pop().expect("unbalanced mask");
            let (a, b) = (label_at(o, n), label_at(c, n));
            partner[a] = b as u8;
            partner[b] = a as u8;
        }
    }
    debug_assert!(stack.is_empty(), "unbalanced mask");
    partner
}

/// Encode a partner array into its Dyck mask.
pub fn encode(partner: &[u8], n: usize) -> u64 {
    let mut mask: u64 = 0;
    for a in 0..2 * n {
        let b = partner[a] as usize;
        if a < b {
            let (ca, cb) = (pos(a, n), pos(b, n));
            mask |= 1u64 << ca.min(cb);
        }
    }
    mask
}

/// Enumerate all Dyck masks of length 2n in a fixed (opener-first
/// depth-first) order. |result| = Catalan(n).
fn gen_masks(n: usize) -> Vec<u64> {
    let two_n = 2 * n;
    let mut out = Vec::with_capacity(catalan(n) as usize);
    // iterative DFS: (position, open_count, mask)
    let mut stack: Vec<(usize, usize, u64)> = vec![(0, 0, 0)];
    while let Some((c, open, mask)) = stack.pop() {
        if c == two_n {
            debug_assert_eq!(open, 0);
            out.push(mask);
            continue;
        }
        // push closer first so opener is explored first (LIFO)
        if open > 0 {
            stack.push((c + 1, open - 1, mask));
        }
        // opener allowed only if the remaining positions can close it
        if open + 1 <= two_n - c - 1 {
            stack.push((c + 1, open + 1, mask | (1u64 << c)));
        }
    }
    out
}

/// Union-find over a fixed node set with loop counting: each edge that
/// joins two already-connected nodes closes exactly one loop
/// (degree ≤ 2 multigraph).
struct Uf {
    p: Vec<u16>,
    loops: u32,
}

impl Uf {
    fn new(size: usize) -> Self {
        Uf { p: (0..size as u16).collect(), loops: 0 }
    }
    fn find(&mut self, mut x: u16) -> u16 {
        while self.p[x as usize] != x {
            self.p[x as usize] = self.p[self.p[x as usize] as usize];
            x = self.p[x as usize];
        }
        x
    }
    fn union(&mut self, a: u16, b: u16) {
        let (ra, rb) = (self.find(a), self.find(b));
        if ra == rb {
            self.loops += 1;
        } else {
            self.p[ra as usize] = rb;
        }
    }
}

/// Generic diagram composition: stack `top` above `bot` (top's bottom row
/// glued to bot's top row). Returns (result partner array, closed loops).
/// Node ids: top's labels as-is (0..2n), bot's labels shifted by +n
/// (so bot-top j ↦ n+j = top-bottom j, bot-bottom j ↦ 2n+j).
pub fn compose(top: &[u8], bot: &[u8], n: usize) -> (Vec<u8>, u32) {
    let mut uf = Uf::new(3 * n);
    for a in 0..2 * n {
        let b = top[a] as usize;
        if a < b {
            uf.union(a as u16, b as u16);
        }
    }
    for a in 0..2 * n {
        let b = bot[a] as usize;
        if a < b {
            uf.union((a + n) as u16, (b + n) as u16);
        }
    }
    // externals: top-top labels 0..n (ids 0..n), bot-bottom labels n..2n
    // (ids 2n..3n). Each external-bearing component has exactly 2.
    let mut first_ext: FxHashMap<u16, usize> = FxHashMap::default();
    let mut partner = vec![0u8; 2 * n];
    for j in 0..2 * n {
        let (id, label) = if j < n {
            (j as u16, j)
        } else {
            ((j + n) as u16, j)
        };
        let root = uf.find(id);
        if let Some(&other) = first_ext.get(&root) {
            partner[label] = other as u8;
            partner[other] = label as u8;
        } else {
            first_ext.insert(root, label);
        }
    }
    (partner, uf.loops)
}

/// Right-multiplication by U_i (1-indexed), specialized closed form:
/// with x = partner(n+i−1), y = partner(n+i) in d —
/// if x == n+i the bottom arc already matches U's top arc: result = d,
/// one loop closes; otherwise re-pair {x,y} + {n+i−1, n+i}, no loop.
#[inline]
pub fn mul_u(partner: &mut [u8], i: usize, n: usize) -> u32 {
    let (p1, p2) = (n + i - 1, n + i);
    let x = partner[p1] as usize;
    let y = partner[p2] as usize;
    if x == p2 {
        return 1;
    }
    partner[x] = y as u8;
    partner[y] = x as u8;
    partner[p1] = p2 as u8;
    partner[p2] = p1 as u8;
    0
}

/// Loop count of the Markov closure of a diagram (join label j to n+j
/// for every j; every component is a loop).
pub fn closure_loops(partner: &[u8], n: usize) -> u32 {
    let mut seen = vec![false; 2 * n];
    let mut loops = 0u32;
    for start in 0..2 * n {
        if seen[start] {
            continue;
        }
        loops += 1;
        // alternate diagram-arc / closure-arc steps until the cycle closes
        let mut a = start;
        loop {
            seen[a] = true;
            let b = partner[a] as usize; // diagram arc
            seen[b] = true;
            let c = if b < n { b + n } else { b - n }; // closure arc
            if c == start {
                break;
            }
            a = c;
        }
    }
    loops
}

/// Precomputed TL_n transfer engine: basis masks, index map, packed
/// right-multiplication tables (bit 31 = loop flag, low bits = target
/// index), and Markov-closure loop counts.
pub struct TlEngine {
    pub n: usize,
    pub dim: usize,
    pub masks: Vec<u64>,
    pub index: FxHashMap<u64, u32>,
    /// tables[g−1][i] = (lp << 31) | j  for basis[i]·U_g = δ^lp basis[j]
    pub tables: Vec<Vec<u32>>,
    pub closure: Vec<u8>,
    pub ident: u32,
}

const LP_BIT: u32 = 1 << 31;

impl TlEngine {
    pub fn new(n: usize) -> Self {
        assert!(n >= 2 && n <= 15, "TlEngine supports 2 ≤ n ≤ 15");
        let masks = gen_masks(n);
        let dim = masks.len();
        assert_eq!(dim as u64, catalan(n), "basis count != Catalan(n)");
        let mut index = FxHashMap::with_capacity_and_hasher(dim, Default::default());
        for (i, &m) in masks.iter().enumerate() {
            index.insert(m, i as u32);
        }
        // identity diagram
        let mut ident_partner = vec![0u8; 2 * n];
        for j in 0..n {
            ident_partner[j] = (n + j) as u8;
            ident_partner[n + j] = j as u8;
        }
        let ident = index[&encode(&ident_partner, n)];
        // right-multiplication tables via the specialized U rule
        let tables: Vec<Vec<u32>> = (1..n)
            .map(|g| {
                masks
                    .par_iter()
                    .map(|&m| {
                        let mut d = decode(m, n);
                        let lp = mul_u(&mut d, g, n);
                        let j = index[&encode(&d, n)];
                        if lp == 1 { j | LP_BIT } else { j }
                    })
                    .collect()
            })
            .collect();
        let closure: Vec<u8> = masks
            .par_iter()
            .map(|&m| closure_loops(&decode(m, n), n) as u8)
            .collect();
        TlEngine { n, dim, masks, index, tables, closure, ident }
    }
}

/// Numeric context at a fixed real q: A = q^{−1/2}, δ = −A²−A⁻².
pub struct QCtx {
    pub prec: u32,
    pub q: Float,
    pub a: Float,
    pub a_inv: Float,
    pub delta: Float,
}

impl QCtx {
    pub fn new(q_dec: &str, prec: u32) -> Self {
        let q = Float::with_val(prec, Float::parse(q_dec).expect("bad q decimal"));
        assert!(q > 0u32, "q must be positive real");
        let a = q.clone().sqrt().recip(); // q^{-1/2}
        let a_inv = a.clone().recip();
        let a2 = a.clone().square();
        let ainv2 = a_inv.clone().square();
        let delta = -(a2 + ainv2);
        QCtx { prec, q, a, a_inv, delta }
    }
}

/// Dense transfer state over a TlEngine basis.
pub struct Transfer<'e> {
    pub eng: &'e TlEngine,
    pub ctx: &'e QCtx,
    /// δ^{closure[i]−1} weights for the Markov closure sum.
    weights: Vec<Float>,
}

impl<'e> Transfer<'e> {
    pub fn new(eng: &'e TlEngine, ctx: &'e QCtx) -> Self {
        let max_loops = *eng.closure.iter().max().unwrap() as usize;
        let mut pows = Vec::with_capacity(max_loops);
        pows.push(Float::with_val(ctx.prec, 1)); // δ^0
        for k in 1..max_loops {
            let next = (&pows[k - 1] * &ctx.delta).complete(ctx.prec);
            pows.push(next);
        }
        let weights: Vec<Float> = eng
            .closure
            .par_iter()
            .map(|&c| pows[(c - 1) as usize].clone())
            .collect();
        Transfer { eng, ctx, weights }
    }

    pub fn ident_vec(&self) -> Vec<Float> {
        let mut v = self.zero_vec();
        v[self.eng.ident as usize] = Float::with_val(self.ctx.prec, 1);
        v
    }

    pub fn zero_vec(&self) -> Vec<Float> {
        (0..self.eng.dim)
            .map(|_| Float::with_val(self.ctx.prec, 0))
            .collect()
    }

    /// out = in · σ_g (signed braid generator, |g| 1-indexed):
    /// σ = cA·1 + cB·U with (cA, cB) = (A, A⁻¹) for g > 0, swapped for
    /// g < 0. Parallel scatter-by-target-range: each thread owns a range
    /// of targets and scans the full table, so no write conflicts.
    pub fn apply_signed(&self, vin: &[Float], vout: &mut [Float], g: i32) {
        let gi = (g.unsigned_abs() as usize) - 1;
        let (ca, cb) = if g > 0 {
            (&self.ctx.a, &self.ctx.a_inv)
        } else {
            (&self.ctx.a_inv, &self.ctx.a)
        };
        let cbd = (cb * &self.ctx.delta).complete(self.ctx.prec);
        let tbl = &self.eng.tables[gi];
        let prec = self.ctx.prec;
        let dim = self.eng.dim;
        let nchunks = rayon::current_num_threads().max(1);
        let chunk = dim.div_ceil(nchunks);
        vout.par_chunks_mut(chunk).enumerate().for_each(|(ci, out)| {
            let lo = ci * chunk;
            let hi = lo + out.len();
            let mut tmp = Float::new(prec);
            for (o, vi) in out.iter_mut().zip(&vin[lo..hi]) {
                o.assign_ref_mul(vi, ca, prec);
            }
            for (k, &e) in tbl.iter().enumerate() {
                let j = (e & !LP_BIT) as usize;
                if j < lo || j >= hi {
                    continue;
                }
                let coef = if e & LP_BIT != 0 { &cbd } else { cb };
                tmp.assign((&vin[k] * coef).complete(prec));
                out[j - lo] += &tmp;
            }
        });
    }

    /// out = in · U_g (bare TL generator, 1-indexed).
    pub fn apply_bare_u(&self, vin: &[Float], vout: &mut [Float], g: usize) {
        let tbl = &self.eng.tables[g - 1];
        let prec = self.ctx.prec;
        let dim = self.eng.dim;
        let delta = &self.ctx.delta;
        let nchunks = rayon::current_num_threads().max(1);
        let chunk = dim.div_ceil(nchunks);
        vout.par_chunks_mut(chunk).enumerate().for_each(|(ci, out)| {
            let lo = ci * chunk;
            let hi = lo + out.len();
            let mut tmp = Float::new(prec);
            for o in out.iter_mut() {
                o.assign(0);
            }
            for (k, &e) in tbl.iter().enumerate() {
                let j = (e & !LP_BIT) as usize;
                if j < lo || j >= hi {
                    continue;
                }
                if e & LP_BIT != 0 {
                    tmp.assign((&vin[k] * delta).complete(prec));
                    out[j - lo] += &tmp;
                } else {
                    out[j - lo] += &vin[k];
                }
            }
        });
    }

    /// Markov-closure value Σ_i v[i]·δ^{closure[i]−1}.
    pub fn closure_sum(&self, v: &[Float]) -> Float {
        let prec = self.ctx.prec;
        v.par_iter()
            .zip(&self.weights)
            .fold(
                || Float::with_val(prec, 0),
                |mut acc, (c, w)| {
                    acc += (c * w).complete(prec);
                    acc
                },
            )
            .reduce(|| Float::with_val(prec, 0), |mut a, b| {
                a += &b;
                a
            })
    }
}

/// Helper trait: out.assign(a * b) without allocation.
trait AssignRefMul {
    fn assign_ref_mul(&mut self, a: &Float, b: &Float, prec: u32);
}
impl AssignRefMul for Float {
    #[inline]
    fn assign_ref_mul(&mut self, a: &Float, b: &Float, prec: u32) {
        self.assign((a * b).complete(prec));
    }
}

use rug::Assign;

/// c-cable of a braid word: σ_i ↦ the c² block of adjacent
/// transpositions (rows moving the i-th strand bundle over the
/// (i+1)-th); inverses reversed and negated. Port of
/// `qbeta_5two_higher_cable_qstar_probe.cable`.
pub fn cable(word: &[i32], c: usize) -> Vec<i32> {
    let mut out = Vec::with_capacity(word.len() * c * c);
    for &g in word {
        let i = g.unsigned_abs() as usize;
        let base = c * (i - 1);
        let mut block = Vec::with_capacity(c * c);
        for r in 0..c {
            let start = base + c - r;
            for s in 0..c {
                block.push((start + s) as i32);
            }
        }
        if g > 0 {
            out.extend(block);
        } else {
            out.extend(block.iter().rev().map(|&x| -x));
        }
    }
    out
}

/// Jones–Wenzl projector e_m expanded in the TL_m **diagram basis**:
/// returns the coefficient vector over `small.masks` order. Built by the
/// Wenzl recursion with full diagram-algebra products (the small engine's
/// generic pair-composition), then self-tested: absorption U_i·e_m ≈ 0
/// for every i, idempotence e_m² ≈ e_m.
pub fn jw_diagram_coeffs(small: &TlEngine, ctx: &QCtx) -> Vec<Float> {
    let m = small.n;
    let dim = small.dim;
    let prec = ctx.prec;
    // δ-Chebyshev brackets [k]: [1]=1, [2]=δ, [k+1]=δ[k]−[k−1]
    let mut br = vec![Float::with_val(prec, 0), Float::with_val(prec, 1)];
    for k in 2..=m + 1 {
        let next = (&ctx.delta * &br[k - 1]).complete(prec) - &br[k - 2];
        br.push(next);
    }
    // full pair-composition table on the small engine (dim² entries)
    let partners: Vec<Vec<u8>> = small.masks.iter().map(|&mk| decode(mk, m)).collect();
    let pair_tab: Vec<Vec<(u32, u8)>> = partners
        .par_iter()
        .map(|a| {
            partners
                .iter()
                .map(|b| {
                    let (d, lp) = compose(a, b, m);
                    (small.index[&encode(&d, m)], lp as u8)
                })
                .collect()
        })
        .collect();
    let dpow = |l: u8| -> Float {
        let mut p = Float::with_val(prec, 1);
        for _ in 0..l {
            p *= &ctx.delta;
        }
        p
    };
    let mul = |x: &[Float], y: &[Float]| -> Vec<Float> {
        let tiny = Float::with_val(prec, Float::parse("1e-45").unwrap());
        let mut out: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
        for (ia, xa) in x.iter().enumerate() {
            if xa.clone().abs() < tiny {
                continue;
            }
            for (ib, yb) in y.iter().enumerate() {
                if yb.clone().abs() < tiny {
                    continue;
                }
                let (j, lp) = pair_tab[ia][ib];
                let term = (xa * yb).complete(prec) * dpow(lp);
                out[j as usize] += term;
            }
        }
        out
    };
    // e_1 = identity
    let mut e: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
    e[small.ident as usize] = Float::with_val(prec, 1);
    for k in 2..=m {
        // e_k = e_{k−1} − ([k−1]/[k])·e_{k−1}·U_{k−1}·e_{k−1}
        let coef = (&br[k - 1] / &br[k]).complete(prec);
        // e·U_{k−1} via the right-multiplication table (cheap)
        let mut eu: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
        let tbl = &small.tables[k - 2];
        for (i, c) in e.iter().enumerate() {
            let ent = tbl[i];
            let j = (ent & !LP_BIT) as usize;
            let term = if ent & LP_BIT != 0 {
                (c * &ctx.delta).complete(prec)
            } else {
                c.clone()
            };
            eu[j] += term;
        }
        let eue = mul(&eu, &e);
        for (ei, t) in e.iter_mut().zip(eue) {
            *ei -= (&coef * &t).complete(prec);
        }
    }
    // self-tests: absorption + idempotence (fail loudly — these gate the
    // diagram-basis normalization against the raw Wenzl expansion)
    let tol = Float::with_val(prec, Float::parse("1e-30").unwrap());
    for g in 1..m {
        let mut ue: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
        // U_g·e = (eᵀ as left factor): use full products: U_g in diagram basis
        let mut ug: Vec<Float> = (0..dim).map(|_| Float::with_val(prec, 0)).collect();
        let mut up = vec![0u8; 2 * m];
        for j in 0..m {
            up[j] = (m + j) as u8;
            up[m + j] = j as u8;
        }
        let lp = mul_u(&mut up, g, m);
        assert_eq!(lp, 0);
        ug[small.index[&encode(&up, m)] as usize] = Float::with_val(prec, 1);
        let prod = mul(&ug, &e);
        for (o, p) in ue.iter_mut().zip(prod) {
            *o = p;
        }
        let maxabs = ue
            .iter()
            .map(|c| c.clone().abs())
            .fold(Float::with_val(prec, 0), |a, b| if b > a { b } else { a });
        assert!(maxabs < tol, "JW absorption U_{g}·e_{m} failed: {maxabs}");
    }
    let ee = mul(&e, &e);
    for (a, b) in ee.iter().zip(&e) {
        let d = (a - b).complete(prec).abs();
        assert!(d < tol, "JW idempotence e_{m}² failed: {d}");
    }
    e
}

/// Loop-free reduced word (1-indexed U generators) for every basis
/// diagram, by BFS from the identity over lp = 0 right-multiplication
/// edges. Every TL diagram has such a word (Jones normal form).
pub fn reduced_words(small: &TlEngine) -> Vec<Vec<u8>> {
    let dim = small.dim;
    let mut words: Vec<Option<Vec<u8>>> = vec![None; dim];
    words[small.ident as usize] = Some(vec![]);
    let mut queue = std::collections::VecDeque::from([small.ident as usize]);
    while let Some(i) = queue.pop_front() {
        for g in 1..small.n {
            let e = small.tables[g - 1][i];
            if e & LP_BIT != 0 {
                continue;
            }
            let j = (e & !LP_BIT) as usize;
            if words[j].is_none() {
                let mut w = words[i].clone().unwrap();
                w.push(g as u8);
                words[j] = Some(w);
                queue.push_back(j);
            }
        }
    }
    words
        .into_iter()
        .map(|w| w.expect("BFS did not reach every diagram loop-free"))
        .collect()
}

/// Raw (unframed) colored-Jones datum J'_{cN+1} of the closure of
/// `word` ∈ B_{k_strands}, via the cN-cable + e_{cN} insertion:
/// numerator = ⟨cable(word)·e_{cN}⟩ / denominator ⟨e_{cN}⟩, both with
/// the δ^{loops−1} closure normalization. Port of
/// `qbeta_5two_n5_cable_qstar_probe.Jp` with the diagram-basis JW.
pub struct JpEvaluator {
    pub big: TlEngine,
    pub small: TlEngine,
    pub cn: usize,
}

impl JpEvaluator {
    pub fn new(k_strands: usize, cn: usize) -> Self {
        let big = TlEngine::new(cn * k_strands);
        let small = TlEngine::new(cn);
        JpEvaluator { big, small, cn }
    }

    pub fn jp(&self, word: &[i32], q_dec: &str, prec: u32) -> Float {
        let ctx = QCtx::new(q_dec, prec);
        let jw = jw_diagram_coeffs(&self.small, &ctx);
        let rw = reduced_words(&self.small);
        let tiny = Float::with_val(prec, Float::parse("1e-40").unwrap());

        // numerator on the big engine
        let tr = Transfer::new(&self.big, &ctx);
        let cw = cable(word, self.cn);
        let mut vec_a = tr.ident_vec();
        let mut vec_b = tr.zero_vec();
        for &g in &cw {
            tr.apply_signed(&vec_a, &mut vec_b, g);
            std::mem::swap(&mut vec_a, &mut vec_b);
        }
        // vec_a = post-cable base vector; apply each JW diagram term
        let mut scratch = tr.zero_vec();
        let mut scratch2 = tr.zero_vec();
        let mut num = Float::with_val(prec, 0);
        for (di, coef) in jw.iter().enumerate() {
            if coef.clone().abs() < tiny {
                continue;
            }
            for (s, a) in scratch.iter_mut().zip(&vec_a) {
                s.assign(a);
            }
            for &g in &rw[di] {
                tr.apply_bare_u(&scratch, &mut scratch2, g as usize);
                std::mem::swap(&mut scratch, &mut scratch2);
            }
            num += (coef * &tr.closure_sum(&scratch)).complete(prec);
        }

        // denominator ⟨e_{cN}⟩ on the small engine (the JW diagram-basis
        // vector IS the identity-applied vector)
        let tr_s = Transfer::new(&self.small, &ctx);
        let den = tr_s.closure_sum(&jw);
        num / den
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn catalan_dims() {
        for (n, c) in [(2, 2u64), (3, 5), (4, 14), (5, 42), (9, 4862), (12, 208012)] {
            assert_eq!(catalan(n), c);
        }
        assert_eq!(catalan(15), 9_694_845);
    }

    #[test]
    fn engine_dims_and_specialized_rule_matches_generic_compose() {
        for n in [3usize, 4, 6] {
            let eng = TlEngine::new(n);
            assert_eq!(eng.dim as u64, catalan(n));
            // U_g diagrams
            for g in 1..n {
                let mut up = vec![0u8; 2 * n];
                for j in 0..n {
                    up[j] = (n + j) as u8;
                    up[n + j] = j as u8;
                }
                assert_eq!(mul_u(&mut up, g, n), 0);
                for (i, &mk) in eng.masks.iter().enumerate() {
                    let d = decode(mk, n);
                    let (gen_d, gen_lp) = compose(&d, &up, n);
                    let mut spec = d.clone();
                    let spec_lp = mul_u(&mut spec, g, n);
                    assert_eq!(encode(&gen_d, n), encode(&spec, n), "n={n} g={g} i={i}");
                    assert_eq!(gen_lp, spec_lp, "n={n} g={g} i={i}");
                }
            }
        }
    }

    #[test]
    fn tl_relations_via_tables() {
        // U_i² = δ·U_i and U_i U_{i±1} U_i = U_i as index/loop bookkeeping
        let n = 5;
        let eng = TlEngine::new(n);
        for g in 1..n {
            for i in 0..eng.dim {
                let e1 = eng.tables[g - 1][i];
                let j1 = (e1 & !LP_BIT) as usize;
                let e2 = eng.tables[g - 1][j1];
                // second application must close exactly one loop and fix j1
                assert_eq!((e2 & !LP_BIT) as usize, j1);
                assert_eq!(e2 & LP_BIT, LP_BIT);
            }
        }
        for g in 1..n - 1 {
            for i in 0..eng.dim {
                // U_g U_{g+1} U_g = U_g : net loops 0, same target as U_g
                let a = eng.tables[g - 1][i];
                let b = eng.tables[g][(a & !LP_BIT) as usize];
                let c = eng.tables[g - 1][(b & !LP_BIT) as usize];
                assert_eq!(c & !LP_BIT, a & !LP_BIT);
                assert_eq!((b & LP_BIT) | (c & LP_BIT), 0);
            }
        }
    }

    #[test]
    fn closure_of_identity_is_n_loops() {
        for n in [3usize, 5] {
            let eng = TlEngine::new(n);
            assert_eq!(eng.closure[eng.ident as usize] as usize, n);
        }
    }

    #[test]
    fn braid_relation_bracket() {
        // ⟨closure(σ1σ2σ1)⟩ = ⟨closure(σ2σ1σ2)⟩ on 3 strands
        let eng = TlEngine::new(3);
        let ctx = QCtx::new("1.07", 128);
        let tr = Transfer::new(&eng, &ctx);
        let run = |word: &[i32]| -> Float {
            let mut a = tr.ident_vec();
            let mut b = tr.zero_vec();
            for &g in word {
                tr.apply_signed(&a, &mut b, g);
                std::mem::swap(&mut a, &mut b);
            }
            tr.closure_sum(&a)
        };
        let x = run(&[1, 2, 1]);
        let y = run(&[2, 1, 2]);
        let d = (&x - &y).complete(128).abs();
        assert!(d < Float::with_val(128, Float::parse("1e-30").unwrap()), "{d}");
    }

    #[test]
    fn jw_denominator_is_chebyshev_bracket() {
        // δ·⟨e_m⟩ = [m+1]: the δ^{loops−1} closure normalization divides
        // the standard δ-per-loop closure (= [m+1]) by one δ
        // (hand-check m=1: ⟨1⟩ = 1 = [2]/δ; m=2: δ − 1/δ = [3]/δ).
        for m in [2usize, 3, 4, 5] {
            let small = TlEngine::new(m);
            let ctx = QCtx::new("1.11", 160);
            let jw = jw_diagram_coeffs(&small, &ctx);
            let tr = Transfer::new(&small, &ctx);
            let den_delta = tr.closure_sum(&jw) * &ctx.delta;
            let mut br = vec![
                Float::with_val(160, 0),
                Float::with_val(160, 1),
            ];
            for k in 2..=m + 1 {
                let next = (&ctx.delta * &br[k - 1]).complete(160) - &br[k - 2];
                br.push(next);
            }
            let d = (&den_delta - &br[m + 1]).complete(160).abs();
            assert!(d < Float::with_val(160, Float::parse("1e-30").unwrap()), "m={m}: {d}");
        }
    }

    #[test]
    fn reduced_words_cover_basis() {
        for m in [3usize, 4, 5] {
            let small = TlEngine::new(m);
            let words = reduced_words(&small);
            assert_eq!(words.len(), small.dim);
            // replay each word from identity: must land on its diagram, loop-free
            for (i, w) in words.iter().enumerate() {
                let mut idx = small.ident as usize;
                for &g in w {
                    let e = small.tables[g as usize - 1][idx];
                    assert_eq!(e & LP_BIT, 0);
                    idx = (e & !LP_BIT) as usize;
                }
                assert_eq!(idx, i);
            }
        }
    }

    #[test]
    fn unknot_writhe1_framing_n3() {
        // fr₂ = 1/J'₃(unknot, writhe 1) = +q⁴ (A5.2-measured, cN=2)
        let ev = JpEvaluator::new(2, 2);
        let q = "1.11";
        let jp = ev.jp(&[1], q, 160);
        let fr = jp.clone().recip();
        let ctx = QCtx::new(q, 160);
        let q4 = ctx.q.clone().square().square();
        let d = ((&fr - &q4).complete(160) / q4).abs();
        assert!(d < Float::with_val(160, Float::parse("1e-25").unwrap()), "fr₂ != q⁴: {d}");
    }
}
