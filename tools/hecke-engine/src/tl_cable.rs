//! Temperley–Lieb cable engine for the certified categorical q\*-test.
//!
//! This is the optimized Rust port of the Python reference probes
//! (`computations/probes/qbeta_5two_n{3,5}_cable_qstar_probe.py`,
//! `qbeta_5two_higher_cable_qstar_probe.py`) used to certify the categorical
//! q\*-test at N = 3, 4, 5 (merged PRs #3927, #4032, #4034). It exists to push
//! the rung to **N = 6** (`cN = 5` cable, TL₁₅ = Catalan(15) = 9 694 845
//! diagrams), which is cost-prohibitive in pure Python.
//!
//! ## Why real arithmetic
//!
//! Every quantity in the colored-Jones computation at a **real** substrate
//! `q` stays real: `A = q^{-1/2}`, `δ = −A² − A⁻²`, the Jones–Wenzl
//! Chebyshev coefficients `[k]_δ`, and the plat/trace closures are all real.
//! The Python reference carries `mpmath.mpc` (complex) purely for uniformity;
//! the imaginary parts are identically zero. Working over `rug::Float`
//! (real MPFR) instead of a complex type halves both the memory footprint of
//! the sparse state vectors and the per-op cost — the decisive optimization
//! for the 9.7M-diagram TL₁₅ pass.
//!
//! ## Diagram model
//!
//! A TL_n diagram is a non-crossing perfect matching of `2n` boundary points.
//! Points are **labels** `0..2n`: `0..n` are the top row (left→right) and
//! `n..2n` are the bottom row, with label `n+j` sitting at circular position
//! `2n−1−j`. A diagram is stored as a partner array `partner[label] = mate`.
//! This mirrors the label convention of the Python `tl_basis` / `tl_compose`
//! so the composition and closure logic is a faithful transcription.
//!
//! Basis ordering is an internal detail: every observable routes through the
//! diagram→index map, and the final colored-Jones value is independent of the
//! enumeration order, so we enumerate in convenient position order.

use rayon::prelude::*;
use rug::ops::Pow;
use rug::Float;
use rustc_hash::FxHashMap;

/// Max boundary points supported: `2 · 15 = 30` (TL₁₅ / N = 6 cable).
pub const MAXP: usize = 30;

/// A diagram as a partner array over labels `0..2n`; entries `≥ 2n` are unused.
pub type Diagram = [u8; MAXP];

/// Working MPFR precision in bits. dps=30 in the Python reference ≈ 100 bits;
/// 192 bits (~58 decimal digits) beats the tightest gate tolerance (1e-18)
/// with a wide margin.
pub const PREC: u32 = 192;

#[inline]
fn f(v: i32) -> Float {
    Float::with_val(PREC, v)
}

// ------------------------- union–find with loop count -------------------------

/// Fixed-capacity union–find over `3n ≤ 45` nodes with closed-loop counting.
/// Each edge that joins two already-connected nodes closes exactly one loop
/// (the multigraph has degree ≤ 2, so this counts cycles correctly).
struct UnionFind {
    parent: [u8; 3 * MAXP],
    loops: u32,
}

impl UnionFind {
    fn new(nodes: usize) -> Self {
        let mut parent = [0u8; 3 * MAXP];
        for (i, p) in parent.iter_mut().enumerate().take(nodes) {
            *p = i as u8;
        }
        UnionFind { parent, loops: 0 }
    }

    #[inline]
    fn find(&mut self, mut x: u8) -> u8 {
        while self.parent[x as usize] != x {
            self.parent[x as usize] = self.parent[self.parent[x as usize] as usize];
            x = self.parent[x as usize];
        }
        x
    }

    #[inline]
    fn union(&mut self, a: u8, b: u8) {
        let ra = self.find(a);
        let rb = self.find(b);
        if ra == rb {
            self.loops += 1;
        } else {
            self.parent[ra as usize] = rb;
        }
    }
}

// ------------------------------- basis enumeration ----------------------------

/// Label sitting at circular position `p` for a `2n`-point diagram:
/// top labels `0..n` occupy positions `0..n`; bottom label `n+j` occupies
/// position `2n−1−j`, i.e. position `p ≥ n` carries label `n + (2n−1−p)`.
#[inline]
fn label_at_pos(p: usize, n: usize) -> u8 {
    if p < n {
        p as u8
    } else {
        (n + (2 * n - 1 - p)) as u8
    }
}

/// All non-crossing perfect matchings of a set of circular positions, as pair
/// lists. Splits on the lowest position `a`: it pairs with some `b` such that
/// the positions strictly *inside* `(a,b)` form an even set matched only among
/// themselves (never crossing the `a–b` chord), and the *outside* is matched
/// independently. This inside/outside separation — not a mere even-count test —
/// is what enforces non-crossing. Direct transcription of the Python
/// `tl_basis` recursion.
fn nc_matchings(avail: &[usize]) -> Vec<Vec<(usize, usize)>> {
    if avail.is_empty() {
        return vec![Vec::new()];
    }
    let a = avail[0]; // lowest position
    let mut out: Vec<Vec<(usize, usize)>> = Vec::new();
    for k in 1..avail.len() {
        let b = avail[k]; // a < b since a is the minimum
        let inside: Vec<usize> = avail[1..]
            .iter()
            .copied()
            .filter(|&x| x != b && a < x && x < b)
            .collect();
        if inside.len() % 2 != 0 {
            continue;
        }
        let outside: Vec<usize> = avail[1..]
            .iter()
            .copied()
            .filter(|&x| x != b && !(a < x && x < b))
            .collect();
        let ins = nc_matchings(&inside);
        let outs = nc_matchings(&outside);
        for ri in &ins {
            for ro in &outs {
                let mut mm = Vec::with_capacity(1 + ri.len() + ro.len());
                mm.push((a, b));
                mm.extend_from_slice(ri);
                mm.extend_from_slice(ro);
                out.push(mm);
            }
        }
    }
    out
}

/// Enumerate the TL_n basis (Catalan(n) non-crossing matchings) as label-space
/// partner arrays, with the diagram→index map.
fn build_basis(n: usize) -> (Vec<Diagram>, FxHashMap<Diagram, u32>) {
    let m = 2 * n;
    let positions: Vec<usize> = (0..m).collect();
    let matchings = nc_matchings(&positions);
    let mut out: Vec<Diagram> = Vec::with_capacity(matchings.len());
    for mm in &matchings {
        let mut d: Diagram = [0u8; MAXP];
        for &(p, q) in mm {
            let la = label_at_pos(p, n) as usize;
            let lb = label_at_pos(q, n) as usize;
            d[la] = lb as u8;
            d[lb] = la as u8;
        }
        out.push(d);
    }
    let mut index: FxHashMap<Diagram, u32> =
        FxHashMap::with_capacity_and_hasher(out.len(), Default::default());
    for (i, d) in out.iter().enumerate() {
        index.insert(*d, i as u32);
    }
    (out, index)
}

/// The identity diagram: through-strands `j — (n+j)`.
fn identity_diagram(n: usize) -> Diagram {
    let mut d: Diagram = [0u8; MAXP];
    for j in 0..n {
        d[j] = (n + j) as u8;
        d[n + j] = j as u8;
    }
    d
}

/// Generator `U_i` (`i ∈ 1..n`) as a diagram: cup–cap joining strands `i−1,i`
/// on both rows, through-strands elsewhere.
fn generator_diagram(i: usize, n: usize) -> Diagram {
    let mut d: Diagram = [0u8; MAXP];
    for j in 0..n {
        if j == i - 1 {
            d[i - 1] = i as u8;
            d[i] = (i - 1) as u8;
            d[n + i - 1] = (n + i) as u8;
            d[n + i] = (n + i - 1) as u8;
        } else if j != i {
            d[j] = (n + j) as u8;
            d[n + j] = j as u8;
        }
    }
    d
}

/// Stack `top` above `bottom` (top's bottom row glued to bottom's top row).
/// Returns the resulting diagram and the number of closed loops.
///
/// Node layout over `3n` ids: `0..n` = top externals, `n..2n` = glue row,
/// `2n..3n` = bottom externals. A top label is its own node id; a bottom
/// label `l` maps to node `n + l`.
fn compose(top: &Diagram, bottom: &Diagram, n: usize) -> (Diagram, u32) {
    let m = 2 * n;
    let mut uf = UnionFind::new(3 * n);
    for a in 0..m {
        let b = top[a] as usize;
        if a < b {
            uf.union(a as u8, b as u8);
        }
    }
    for a in 0..m {
        let b = bottom[a] as usize;
        if a < b {
            uf.union((n + a) as u8, (n + b) as u8);
        }
    }
    // externals: t_j = node j (label j); b_j = node 2n+j (label n+j)
    let mut root_to_label: [i16; 3 * MAXP] = [-1; 3 * MAXP];
    let mut result: Diagram = [0u8; MAXP];
    for j in 0..n {
        for &(node, label) in &[(j, j), (2 * n + j, n + j)] {
            let r = uf.find(node as u8) as usize;
            if root_to_label[r] < 0 {
                root_to_label[r] = label as i16;
            } else {
                let other = root_to_label[r] as usize;
                result[label] = other as u8;
                result[other] = label as u8;
            }
        }
    }
    (result, uf.loops)
}

/// Trace/plat closure loop count of a diagram: connect `j — (n+j)` and count
/// cycles.
fn closure_loops(d: &Diagram, n: usize) -> u32 {
    let m = 2 * n;
    let mut uf = UnionFind::new(m);
    for a in 0..m {
        let b = d[a] as usize;
        if a < b {
            uf.union(a as u8, b as u8);
        }
    }
    for j in 0..n {
        uf.union(j as u8, (n + j) as u8);
    }
    uf.loops
}

// --------------------------------- the engine ---------------------------------

/// Precomputed TL_n data: for each generator `U_i` a destination-index +
/// loop-count table over the whole basis, plus the closure loop count of every
/// basis diagram and the identity's index. The basis and diagram→index map are
/// dropped after construction; only these tables are needed to evaluate.
pub struct TlEngine {
    pub n: usize,
    pub ndiag: usize,
    pub ident_idx: u32,
    /// `tab_idx[g][i]` = index of `U_{g+1}·(diagram i)`; `g ∈ 0..n−1`.
    pub tab_idx: Vec<Vec<u32>>,
    /// `tab_lp[g][i]` = loops closed by that composition.
    pub tab_lp: Vec<Vec<u8>>,
    /// `closure[i]` = closure loop count of diagram `i` (always `≥ 1`).
    pub closure: Vec<u8>,
}

impl TlEngine {
    /// Build the engine for `n` strands. Table construction is parallelized
    /// over the basis with rayon (each diagram's `n−1` generator images are
    /// independent).
    pub fn build(n: usize) -> Self {
        assert!(2 * n <= MAXP, "n={n} exceeds MAXP/2");
        let (basis, index) = build_basis(n);
        let ndiag = basis.len();
        let ident_idx = index[&identity_diagram(n)];

        let gens: Vec<Diagram> = (1..n).map(|i| generator_diagram(i, n)).collect();

        // For each generator, compose against every basis diagram in parallel.
        let mut tab_idx: Vec<Vec<u32>> = Vec::with_capacity(n.saturating_sub(1));
        let mut tab_lp: Vec<Vec<u8>> = Vec::with_capacity(n.saturating_sub(1));
        for u in &gens {
            let col: Vec<(u32, u8)> = basis
                .par_iter()
                .map(|d| {
                    let (dg, lp) = compose(d, u, n);
                    // Composition of two planar diagrams is planar, so `dg` is
                    // always a basis element; a miss would be an engine bug.
                    (index[&dg], lp as u8)
                })
                .collect();
            let (idx_col, lp_col): (Vec<u32>, Vec<u8>) = col.into_iter().unzip();
            tab_idx.push(idx_col);
            tab_lp.push(lp_col);
        }

        let closure: Vec<u8> = basis
            .par_iter()
            .map(|d| closure_loops(d, n) as u8)
            .collect();

        TlEngine {
            n,
            ndiag,
            ident_idx,
            tab_idx,
            tab_lp,
            closure,
        }
    }
}

// ------------------------------ cable + Jones–Wenzl ----------------------------

/// `c`-cable of a signed braid word: `σ_i ↦` the `c²` crossing block that moves
/// bundle `i` over bundle `i+1`. Direct transcription of the Python `cable`.
pub fn cable(word: &[i32], c: usize) -> Vec<i32> {
    let mut out: Vec<i32> = Vec::new();
    for &g in word {
        let i = g.unsigned_abs() as usize;
        let base = c * (i - 1);
        let mut block: Vec<i32> = Vec::with_capacity(c * c);
        for r in 0..c {
            let start = base + c - r;
            for s in 0..c {
                block.push((start + s) as i32);
            }
        }
        if g > 0 {
            out.extend_from_slice(&block);
        } else {
            out.extend(block.iter().rev().map(|x| -x));
        }
    }
    out
}

/// Jones–Wenzl projector `e_m` on `m` strands as `(coefficient, U-word)` terms
/// via the Wenzl recursion `e_k = e_{k−1} − ([k−1]/[k]) e_{k−1} U_{k−1} e_{k−1}`.
/// Coefficients are evaluated at the given real `q` (δ-Chebyshev brackets).
pub fn jw_terms(m: usize, delta: &Float) -> Vec<(Float, Vec<usize>)> {
    // Chebyshev brackets: [0]=0, [1]=1, [k]=δ[k−1]−[k−2].
    let mut br: Vec<Float> = vec![f(0), f(1)];
    for k in 2..m + 2 {
        let v = Float::with_val(PREC, delta * &br[k - 1]) - &br[k - 2];
        br.push(v);
    }
    let mut terms: FxHashMap<Vec<usize>, Float> = FxHashMap::default();
    terms.insert(Vec::new(), f(1));
    for k in 2..=m {
        let coef = Float::with_val(PREC, &br[k - 1] / &br[k]);
        let snapshot: Vec<(Vec<usize>, Float)> =
            terms.iter().map(|(w, c)| (w.clone(), c.clone())).collect();
        for (w1, c1) in &snapshot {
            for (w2, c2) in &snapshot {
                let mut w = Vec::with_capacity(w1.len() + 1 + w2.len());
                w.extend_from_slice(w1);
                w.push(k - 1);
                w.extend_from_slice(w2);
                let delta_c = Float::with_val(PREC, &coef * c1) * c2;
                let e = terms.entry(w).or_insert_with(|| f(0));
                *e -= &delta_c;
            }
        }
    }
    let tol = Float::with_val(PREC, (10f64).powi(-40));
    terms
        .into_iter()
        .filter(|(_, c)| c.clone().abs() > tol)
        .map(|(w, c)| (c, w))
        .collect()
}

// ------------------------ fast dense-f64 colored-Jones ------------------------
//
// The MPFR path above is the high-precision reference (used to validate against
// the certified N=5 witness). For the TL₁₅ (N=6) pass, 192-bit MPFR over 9.7M
// elements is prohibitive (~20 min/Jp, >11 GB). At a real substrate q the
// colored-Jones value is well-conditioned, so an f64 evaluation with **dense**
// state vectors is ~100× faster and ~10× smaller (78 MB/vector vs ~1 GB),
// bringing a full N=6 run to a few minutes. The accumulated f64 error
// (~1e-10) is far below what the 3-point certificate needs (~1e-6); the tight
// control gates (G2/G3) are reported at f64-realistic tolerances.

/// Jones–Wenzl `e_m` terms with f64 coefficients (δ-Chebyshev).
pub fn jw_terms_f64(m: usize, delta: f64) -> Vec<(f64, Vec<usize>)> {
    let mut br = vec![0.0f64, 1.0];
    for k in 2..m + 2 {
        let v = delta * br[k - 1] - br[k - 2];
        br.push(v);
    }
    let mut terms: FxHashMap<Vec<usize>, f64> = FxHashMap::default();
    terms.insert(Vec::new(), 1.0);
    for k in 2..=m {
        let coef = br[k - 1] / br[k];
        let snapshot: Vec<(Vec<usize>, f64)> =
            terms.iter().map(|(w, c)| (w.clone(), *c)).collect();
        for (w1, c1) in &snapshot {
            for (w2, c2) in &snapshot {
                let mut w = Vec::with_capacity(w1.len() + 1 + w2.len());
                w.extend_from_slice(w1);
                w.push(k - 1);
                w.extend_from_slice(w2);
                *terms.entry(w).or_insert(0.0) -= coef * c1 * c2;
            }
        }
    }
    terms
        .into_iter()
        .filter(|(_, c)| c.abs() > 1e-40)
        .map(|(w, c)| (c, w))
        .collect()
}

/// Apply a bare generator `U_{gi+1}` to a dense f64 state, into `out`.
#[inline]
fn apply_generator_f64(v: &[f64], gi: usize, eng: &TlEngine, dpow: &[f64], out: &mut [f64]) {
    out.iter_mut().for_each(|x| *x = 0.0);
    let idx = &eng.tab_idx[gi];
    let lp = &eng.tab_lp[gi];
    for (i, &c) in v.iter().enumerate() {
        if c != 0.0 {
            out[idx[i] as usize] += c * dpow[lp[i] as usize];
        }
    }
}

#[inline]
fn closure_sum_f64(v: &[f64], eng: &TlEngine, dpow: &[f64]) -> f64 {
    let mut t = 0.0;
    for (i, &c) in v.iter().enumerate() {
        if c != 0.0 {
            t += c * dpow[eng.closure[i] as usize - 1];
        }
    }
    t
}

/// Fast f64 colored-Jones `J'_{cN+1}`; dense state, common-prefix optimization,
/// numerator parallelized over Jones–Wenzl terms. See module note above.
pub fn jp_f64(
    word: &[i32],
    k_strands: usize,
    c_n: usize,
    q: f64,
    engines: &FxHashMap<usize, TlEngine>,
) -> f64 {
    let a = q.powf(-0.5);
    let a_inv = 1.0 / a;
    let delta = -a * a - a_inv * a_inv;
    let n = c_n * k_strands;
    let eng = &engines[&n];
    let engd = &engines[&c_n];
    let maxp = n + 2;
    let mut dpow = vec![1.0f64];
    for _ in 1..=maxp {
        dpow.push(dpow.last().unwrap() * delta);
    }

    // ---- apply the cabled braid word once (dense ping-pong buffers) ----
    let cw = cable(word, c_n);
    let mut cur = vec![0.0f64; eng.ndiag];
    let mut nxt = vec![0.0f64; eng.ndiag];
    cur[eng.ident_idx as usize] = 1.0;
    for &g in &cw {
        let gi = g.unsigned_abs() as usize - 1;
        let (c_a, c_b) = if g > 0 { (a, a_inv) } else { (a_inv, a) };
        let idx = &eng.tab_idx[gi];
        let lp = &eng.tab_lp[gi];
        nxt.iter_mut().for_each(|x| *x = 0.0);
        for (i, &c) in cur.iter().enumerate() {
            if c != 0.0 {
                nxt[i] += c * c_a;
                nxt[idx[i] as usize] += c * c_b * dpow[lp[i] as usize];
            }
        }
        std::mem::swap(&mut cur, &mut nxt);
    }

    let ejw = jw_terms_f64(c_n, delta);

    // ---- numerator: parallel over JW terms (read-only shared prefix) ----
    let num: f64 = ejw
        .par_iter()
        .map(|(coef, gword)| {
            let s = if gword.is_empty() {
                closure_sum_f64(&cur, eng, &dpow)
            } else {
                let mut src = vec![0.0f64; eng.ndiag];
                apply_generator_f64(&cur, gword[0] - 1, eng, &dpow, &mut src);
                let mut dst = vec![0.0f64; eng.ndiag];
                for &g in &gword[1..] {
                    apply_generator_f64(&src, g - 1, eng, &dpow, &mut dst);
                    std::mem::swap(&mut src, &mut dst);
                }
                closure_sum_f64(&src, eng, &dpow)
            };
            coef * s
        })
        .sum();

    // ---- denominator: closure of e_{cN} alone on cN strands ----
    let mut den = 0.0;
    let mut sbuf = vec![0.0f64; engd.ndiag];
    let mut dbuf = vec![0.0f64; engd.ndiag];
    for (coef, gword) in &ejw {
        sbuf.iter_mut().for_each(|x| *x = 0.0);
        sbuf[engd.ident_idx as usize] = 1.0;
        for &g in gword {
            apply_generator_f64(&sbuf, g - 1, engd, &dpow, &mut dbuf);
            std::mem::swap(&mut sbuf, &mut dbuf);
        }
        den += coef * closure_sum_f64(&sbuf, engd, &dpow);
    }

    num / den
}

// ----------------------------- colored-Jones Jp -------------------------------

/// Sparse real state vector over a TL basis: `index → coefficient`.
type State = FxHashMap<u32, Float>;

#[inline]
fn add_scaled(map: &mut State, key: u32, val: &Float) {
    match map.get_mut(&key) {
        Some(e) => *e += val,
        None => {
            map.insert(key, val.clone());
        }
    }
}

/// Powers `δ^0 .. δ^maxp` precomputed once per evaluation (δ fixed, integer
/// exponents kept exact including sign).
fn delta_powers(delta: &Float, maxp: usize) -> Vec<Float> {
    let mut v = Vec::with_capacity(maxp + 1);
    v.push(f(1));
    for _ in 1..=maxp {
        v.push(Float::with_val(PREC, v.last().unwrap() * delta));
    }
    v
}

/// Apply one bare generator `U_{gi+1}` to a state (the `('U', g)` insertion of
/// the Python `bracket_closure`): `v[i] ↦ Σ v[i]·δ^{lp} at dest`.
fn apply_generator(v: &State, gi: usize, eng: &TlEngine, dpow: &[Float]) -> State {
    let idx = &eng.tab_idx[gi];
    let lp = &eng.tab_lp[gi];
    let mut new: State = FxHashMap::with_capacity_and_hasher(v.len(), Default::default());
    for (&i, c) in v {
        let j = idx[i as usize];
        let l = lp[i as usize] as usize;
        let val = Float::with_val(PREC, c * &dpow[l]);
        add_scaled(&mut new, j, &val);
    }
    new
}

/// Closure sum `Σ_i v[i]·δ^{closure[i]−1}`.
fn closure_sum(v: &State, eng: &TlEngine, dpow: &[Float]) -> Float {
    let mut tot = f(0);
    for (&i, c) in v {
        let e = eng.closure[i as usize] as usize - 1;
        tot += Float::with_val(PREC, c * &dpow[e]);
    }
    tot
}

/// Threshold below which a parallel scatter is not worth the fold/reduce +
/// map-merge overhead. Tuned so TL₁₂ (support ≤ 208K) stays sequential — it is
/// already fast serially — and only the TL₁₅ prefix (support grows into the
/// millions) pays for parallelism.
const PAR_THRESHOLD: usize = 500_000;

/// One cabled-braid transition step: `v[i] ↦ c_a·v[i] (same i) + c_b·δ^{lp}·v[i]
/// (at dest j)`, summed over collisions. Parallelized over rayon chunks of the
/// source support when the state is large.
fn transition_cable(
    v: &State,
    idx: &[u32],
    lp: &[u8],
    c_a: &Float,
    c_b: &Float,
    dpow: &[Float],
) -> State {
    let step = |acc: &mut State, i: u32, c: &Float| {
        let va = Float::with_val(PREC, c * c_a);
        add_scaled(acc, i, &va);
        let j = idx[i as usize];
        let l = lp[i as usize] as usize;
        let vb = Float::with_val(PREC, c * c_b) * &dpow[l];
        add_scaled(acc, j, &vb);
    };
    if v.len() < PAR_THRESHOLD {
        let mut new: State =
            FxHashMap::with_capacity_and_hasher(v.len() * 2, Default::default());
        for (&i, c) in v {
            step(&mut new, i, c);
        }
        new
    } else {
        v.par_iter()
            .fold(
                || FxHashMap::with_capacity_and_hasher(0, Default::default()),
                |mut acc, (&i, c)| {
                    step(&mut acc, i, c);
                    acc
                },
            )
            .reduce(
                || FxHashMap::with_capacity_and_hasher(0, Default::default()),
                |mut m1, m2| {
                    for (k, val) in m2 {
                        add_scaled(&mut m1, k, &val);
                    }
                    m1
                },
            )
    }
}

/// Raw colored-Jones `J'_{cN+1}` of the closure of `word ∈ B_{k_strands}` via
/// the `cN`-cable + Jones–Wenzl `e_{cN}` insertion, **without** framing factor.
/// `engines[n]` must provide the TL engine on `n = cN·k_strands` strands and
/// `engines[cN]` the denominator engine.
///
/// Common-prefix optimization: the (long) cabled braid word is applied to the
/// state **once**; each Jones–Wenzl term then only appends its short `U`-suffix.
pub fn jp(
    word: &[i32],
    k_strands: usize,
    c_n: usize,
    q: &Float,
    engines: &FxHashMap<usize, TlEngine>,
) -> Float {
    let half = Float::with_val(PREC, -0.5f64);
    let a = Float::with_val(PREC, q.pow(&half)); // A = q^{-1/2}
    let a_inv = Float::with_val(PREC, f(1) / &a);
    let delta = -(Float::with_val(PREC, a.clone().pow(2u32)))
        - Float::with_val(PREC, a_inv.clone().pow(2u32));
    let n = c_n * k_strands;
    let eng = &engines[&n];
    let engd = &engines[&c_n];
    let maxp = n + 2;
    let dpow = delta_powers(&delta, maxp);

    // ---- apply the cabled braid word once ----
    // Each generator step is a scatter over the current support; steps are
    // sequential (each depends on the last) but the inner scatter is
    // parallelized (fold per rayon chunk, then merge). This is the prefix cost
    // that dominates at TL₁₅ (~100–150 cable letters over a support that grows
    // toward the full 9.7M basis).
    let cw = cable(word, c_n);
    let mut v: State = FxHashMap::default();
    v.insert(eng.ident_idx, f(1));
    for &g in &cw {
        let gi = g.unsigned_abs() as usize - 1;
        let (c_a, c_b) = if g > 0 { (&a, &a_inv) } else { (&a_inv, &a) };
        let idx = &eng.tab_idx[gi];
        let lp = &eng.tab_lp[gi];
        v = transition_cable(&v, idx, lp, c_a, c_b, &dpow);
    }

    let ejw = jw_terms(c_n, &delta);

    // ---- numerator: Σ coef · closure(v · U-suffix) ----
    // Embarrassingly parallel over Jones–Wenzl terms: each term applies its own
    // short U-suffix to a *read-only* clone-free view of the shared prefix `v`,
    // then reduces to a scalar. No shared mutation ⇒ near-linear speedup, and
    // this is the second dominant cost at TL₁₅.
    let term_val = |coef: &Float, gword: &[usize]| -> Float {
        let s = if gword.is_empty() {
            closure_sum(&v, eng, &dpow)
        } else {
            let mut vv = apply_generator(&v, gword[0] - 1, eng, &dpow);
            for &g in &gword[1..] {
                vv = apply_generator(&vv, g - 1, eng, &dpow);
            }
            closure_sum(&vv, eng, &dpow)
        };
        Float::with_val(PREC, coef * &s)
    };
    let num: Float = if eng.ndiag >= PAR_THRESHOLD {
        ejw.par_iter()
            .map(|(coef, gword)| term_val(coef, gword))
            .reduce(|| f(0), |x, y| Float::with_val(PREC, x + y))
    } else {
        let mut num = f(0);
        for (coef, gword) in &ejw {
            num += &term_val(coef, gword);
        }
        num
    };

    // ---- denominator: closure of e_{cN} alone on cN strands ----
    let mut den = f(0);
    for (coef, gword) in &ejw {
        let mut vv: State = FxHashMap::default();
        vv.insert(engd.ident_idx, f(1));
        for &g in gword {
            vv = apply_generator(&vv, g - 1, engd, &dpow);
        }
        let s = closure_sum(&vv, engd, &dpow);
        den += Float::with_val(PREC, coef * &s);
    }

    Float::with_val(PREC, &num / &den)
}
