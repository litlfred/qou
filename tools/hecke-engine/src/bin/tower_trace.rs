//! hecke-tower-trace — convention-D Markov trace of the v9 nuclear element,
//! via two-row Young seminormal representations of H_n(q), in MPFR.
//!
//! Rust port of `computations/probes/markov_trace_two_row_tower_probe.py`
//! (read that file for the mathematics).  Summary:
//!
//!   E = prod_{k=1}^{A-1} prod_{i=0}^{k-1} f(type_i, type_k; sigma_i)
//!
//! right-multiplied in that order, strands 0..Z-1 protons, Z..A-1 neutrons,
//! with f = a + b sigma_i:  p-p (0, 1),  n-n (-h, 1),  p-n (-h, 2) (one "pn"
//! doubling each), h = q - 1/q.  Convention D (z = q^3/(q^2+1)) kills every
//! shape with a third row, so
//!
//!   tr(E) = sum_k [n-2k+1]_q / [2]_q^n * chi_{(n-k,k)}(E),   reported / 2^pn.
//!
//! # Algorithm (differs from the Python, same element)
//!
//! The Python lifts DENSE f x f matrices up the Gelfand-Tsetlin tower.  At
//! A = 20 the largest two-row irrep has f = 16796 (2.8e8 entries per matrix),
//! which is out of reach in MPFR.  The trace only needs the DIAGONAL, and the
//! seminormal basis is GT-adapted, so:
//!
//! * a basis vector of level m+1 is a tableau U; its restriction U|m is a
//!   tableau of level m, and the lifted matrix lift(M_m) has row U equal to
//!   row U|m of M_m, embedded on the block of tableaux sharing U's last entry;
//! * hence row U of M_{m+1} = lift(row U|m of M_m) * rho(B_m), where B_m is
//!   the strand-m block of factors.
//!
//! So a depth-first walk over the tree of two-row standard tableaux (root =
//! the 1-box tableau; children = append the next entry to row 0 or row 1)
//! carries ONE row vector per tree node, computed from its parent's in
//! O(m * f) work.  The diagonal entry (M_m)_{UU} = row_U[U] is read off at
//! every node, so the trace at EVERY level m — i.e. every isotope of the
//! neutron chain at fixed Z — comes out of one walk.  Memory is O(A * f) per
//! thread.  Total work ~ sum_m (m-1) * Catalan(m).  Subtrees below a fixed
//! depth are distributed over rayon.
//!
//! Precision: rug::Float throughout; no f64 anywhere in the arithmetic
//! (q is parsed from its decimal string).  Every chain is computed at two
//! working precisions and the agreement is reported.

use rayon::prelude::*;
use rug::ops::Pow;
use rug::{Assign, Float};
use serde_json::{json, Value};
use std::collections::{BTreeMap, HashMap};
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::Mutex;
use std::time::Instant;

const Q0_STR: &str = "1.1099785827513808075916690956107688798744991218736";

/// MPFR precision for `dps` decimal places: ceil(dps * log2(10)) + 32 guard
/// bits, computed in integers (log2(10) < 3.3220).
fn bits_for(dps: u32) -> u32 {
    (dps * 33220 + 9999) / 10000 + 32
}

// ---------------------------------------------------------------- tableaux

/// Two-row standard tableaux for levels 1..=amax, as bitmasks
/// (bit j = row of entry j), grouped by k = length of row 2.
struct Tower {
    /// tabs[m][k] — level m (m boxes), shape (m-k, k)
    tabs: Vec<Vec<Vec<u32>>>,
    /// parent[m][k][j] = (index of tab|_{m-1} in tabs[m-1][k - last], last)
    parent: Vec<Vec<Vec<(usize, u8)>>>,
    /// child[m][k][j][x] = index in tabs[m+1][k+x] (usize::MAX if invalid)
    child: Vec<Vec<Vec<[usize; 2]>>>,
    /// embed[m][k][x] = list of (j, parent_index) for tabs[m][k] with last == x
    embed: Vec<Vec<[Vec<(usize, usize)>; 2]>>,
    /// ops[m][k][i] — action of sigma_i on the level-m shape-k irrep
    ops: Vec<Vec<Vec<Vec<Op>>>>,
}

#[derive(Clone, Copy)]
enum Op {
    /// sigma v_j = q v_j (plus=true) or -1/q v_j
    Diag { j: usize, plus: bool },
    /// pair with axial distance r > 0 at jp: sigma v_jp = a_r v_jp + v_jm,
    /// sigma v_jm = (1 + a_r a_{-r}) v_jp + a_{-r} v_jm
    Pair { jp: usize, jm: usize, r: usize },
}

fn contents(t: u32, m: usize) -> Vec<i64> {
    let mut rowlen = [0i64, 0i64];
    let mut c = Vec::with_capacity(m);
    for j in 0..m {
        let r = ((t >> j) & 1) as usize;
        c.push(rowlen[r] - r as i64);
        rowlen[r] += 1;
    }
    c
}

impl Tower {
    fn new(amax: usize) -> Tower {
        let mut tabs: Vec<Vec<Vec<u32>>> = vec![vec![], vec![vec![0u32]]];
        let mut parent: Vec<Vec<Vec<(usize, u8)>>> = vec![vec![], vec![vec![(0, 0)]]];
        for m in 1..amax {
            let nk = (m + 1) / 2 + 1;
            let mut nt: Vec<Vec<u32>> = vec![vec![]; nk];
            let mut np: Vec<Vec<(usize, u8)>> = vec![vec![]; nk];
            for (k, ts) in tabs[m].iter().enumerate() {
                let r1 = m - k;
                for (idx, &t) in ts.iter().enumerate() {
                    nt[k].push(t);
                    np[k].push((idx, 0));
                    if k + 1 <= r1 {
                        nt[k + 1].push(t | (1 << m));
                        np[k + 1].push((idx, 1));
                    }
                }
            }
            while nt.last().map(|v| v.is_empty()).unwrap_or(false) {
                nt.pop();
                np.pop();
            }
            tabs.push(nt);
            parent.push(np);
        }
        // child + embed
        let mut child: Vec<Vec<Vec<[usize; 2]>>> = Vec::new();
        let mut embed: Vec<Vec<[Vec<(usize, usize)>; 2]>> = Vec::new();
        for m in 0..=amax {
            child.push(
                tabs[m]
                    .iter()
                    .map(|ts| vec![[usize::MAX; 2]; ts.len()])
                    .collect(),
            );
            embed.push(tabs[m].iter().map(|_| [vec![], vec![]]).collect());
        }
        for m in 2..=amax {
            for k in 0..tabs[m].len() {
                for j in 0..tabs[m][k].len() {
                    let (pidx, last) = parent[m][k][j];
                    let pk = k - last as usize;
                    child[m - 1][pk][pidx][last as usize] = j;
                    embed[m][k][last as usize].push((j, pidx));
                }
            }
        }
        // ops
        let mut ops: Vec<Vec<Vec<Vec<Op>>>> = vec![vec![]];
        for m in 1..=amax {
            let mut per_k = Vec::new();
            for ts in tabs[m].iter() {
                let index: HashMap<u32, usize> =
                    ts.iter().enumerate().map(|(j, &t)| (t, j)).collect();
                let conts: Vec<Vec<i64>> = ts.iter().map(|&t| contents(t, m)).collect();
                let mut per_i = Vec::new();
                for i in 0..m.saturating_sub(1) {
                    let mut done = vec![false; ts.len()];
                    let mut v = Vec::new();
                    for j in 0..ts.len() {
                        if done[j] {
                            continue;
                        }
                        let r = conts[j][i + 1] - conts[j][i];
                        if r.abs() == 1 {
                            v.push(Op::Diag { j, plus: r == 1 });
                            done[j] = true;
                            continue;
                        }
                        let t = ts[j];
                        let bi = (t >> i) & 1;
                        let bj = (t >> (i + 1)) & 1;
                        let t2 = (t & !(1 << i) & !(1 << (i + 1))) | (bj << i) | (bi << (i + 1));
                        let j2 = *index.get(&t2).expect("swapped tableau must be standard");
                        let (jp, jm, rr) = if r > 0 { (j, j2, r) } else { (j2, j, -r) };
                        v.push(Op::Pair { jp, jm, r: rr as usize });
                        done[j] = true;
                        done[j2] = true;
                    }
                    per_i.push(v);
                }
                per_k.push(per_i);
            }
            ops.push(per_k);
        }
        Tower { tabs, parent, child, embed, ops }
    }
}

// ---------------------------------------------------------------- scalars

struct Scalars {
    prec: u32,
    q: Float,
    h: Float,
    z_d: Float,
}

impl Scalars {
    fn new(prec: u32) -> Scalars {
        let q = Float::with_val(prec, Float::parse(Q0_STR).expect("q0 parses"));
        let qi = Float::with_val(prec, 1u32) / &q;
        let h = Float::with_val(prec, &q - &qi);
        let q2 = Float::with_val(prec, &q * &q);
        let q3 = Float::with_val(prec, &q2 * &q);
        let z_d = q3 / (q2 + 1u32);
        Scalars { prec, q, h, z_d }
    }
    fn f(&self, x: u32) -> Float {
        Float::with_val(self.prec, x)
    }
    /// alpha(r) = (q - 1/q) / (1 - q^{-2r}), r a nonzero integer
    fn alpha(&self, r: i64) -> Float {
        let qp = Float::with_val(self.prec, (&self.q).pow(-2 * r as i32));
        Float::with_val(self.prec, &self.h / (1u32 - qp))
    }
    fn qint(&self, m: i64) -> Float {
        let a = Float::with_val(self.prec, (&self.q).pow(m as i32));
        let b = Float::with_val(self.prec, (&self.q).pow(-(m as i32)));
        Float::with_val(self.prec, (a - b) / &self.h)
    }
    /// convention-D weight of the two-row shape (n-k, k)
    fn weight(&self, n: usize, k: usize) -> Float {
        let num = self.qint(n as i64 - 2 * k as i64 + 1);
        let den = Float::with_val(self.prec, self.qint(2).pow(n as u32));
        num / den
    }
}

/// Precomputed coefficients of rho(a + b sigma) for one (a, b).
struct Coefs {
    diag_plus: Float,
    diag_minus: Float,
    /// per r (index r, r >= 2): (c11, c12, c21, c22):
    /// new x = c11 x + c12 y, new y = c21 x + c22 y   (x at jp, y at jm)
    pair: Vec<[Float; 4]>,
}

impl Coefs {
    fn new(s: &Scalars, a: &Float, b: &Float, rmax: usize) -> Coefs {
        let p = s.prec;
        let qi = Float::with_val(p, 1u32) / &s.q;
        let diag_plus = Float::with_val(p, a + Float::with_val(p, b * &s.q));
        let diag_minus = Float::with_val(p, a - Float::with_val(p, b * &qi));
        let mut pair = Vec::new();
        for r in 0..=rmax {
            if r < 2 {
                pair.push([s.f(0), s.f(0), s.f(0), s.f(0)]);
                continue;
            }
            let ar = s.alpha(r as i64);
            let am = s.alpha(-(r as i64));
            let c = Float::with_val(p, 1u32 + Float::with_val(p, &ar * &am));
            let c11 = Float::with_val(p, a + Float::with_val(p, b * &ar));
            let c12 = b.clone();
            let c21 = Float::with_val(p, b * &c);
            let c22 = Float::with_val(p, a + Float::with_val(p, b * &am));
            pair.push([c11, c12, c21, c22]);
        }
        Coefs { diag_plus, diag_minus, pair }
    }
}

/// v <- v * rho(a + b sigma_i), in place.  tmp: scratch Floats (zero heap alloc).
#[inline]
fn apply(
    v: &mut [Float],
    ops: &[Op],
    c: &Coefs,
    t1: &mut Float,
    t2: &mut Float,
    t3: &mut Float,
) {
    for op in ops {
        match *op {
            Op::Diag { j, plus } => {
                v[j] *= if plus { &c.diag_plus } else { &c.diag_minus };
            }
            Op::Pair { jp, jm, r } => {
                let k = &c.pair[r];
                {
                    let x = &v[jp];
                    let y = &v[jm];
                    t1.assign(&k[0] * x);
                    t3.assign(&k[1] * y);
                    *t1 += &*t3;
                    t2.assign(&k[2] * x);
                    t3.assign(&k[3] * y);
                    *t2 += &*t3;
                }
                std::mem::swap(&mut v[jp], t1);
                std::mem::swap(&mut v[jm], t2);
            }
        }
    }
}

// ---------------------------------------------------------------- self-check

fn identity_rows(d: usize, prec: u32) -> Vec<Vec<Float>> {
    (0..d)
        .map(|r| (0..d).map(|c| Float::with_val(prec, (r == c) as u32)).collect())
        .collect()
}

fn mat_apply(m: &mut [Vec<Float>], ops: &[Op], c: &Coefs, prec: u32) {
    let mut t1 = Float::new(prec);
    let mut t2 = Float::new(prec);
    let mut t3 = Float::new(prec);
    for row in m.iter_mut() {
        apply(row, ops, c, &mut t1, &mut t2, &mut t3);
    }
}

fn max_diff(a: &[Vec<Float>], b: &[Vec<Float>], prec: u32) -> Float {
    let mut w = Float::with_val(prec, 0u32);
    for (ra, rb) in a.iter().zip(b) {
        for (x, y) in ra.iter().zip(rb) {
            let d = Float::with_val(prec, x - y).abs();
            if d > w {
                w = d;
            }
        }
    }
    w
}

fn diag_sum(m: &[Vec<Float>], prec: u32) -> Float {
    let mut s = Float::with_val(prec, 0u32);
    for (j, row) in m.iter().enumerate() {
        s += &row[j];
    }
    s
}

/// Hecke relation, braid relation, tr(1) = 1, tr(s_0..s_{n-2}) = z^{n-1},
/// tr(s0 s1 s0) = h z^2 + z, on every two-row irrep up to nmax.
fn self_check(s: &Scalars, tw: &Tower, nmax: usize) -> Float {
    let p = s.prec;
    let zero = s.f(0);
    let one = s.f(1);
    let sig = Coefs::new(s, &zero, &one, nmax);
    let hplus1 = Coefs::new(s, &one, &s.h, nmax); // 1 + h sigma
    let mut worst = s.f(0);
    let bump = |w: &mut Float, d: Float| {
        if d > *w {
            *w = d;
        }
    };
    for n in 2..=nmax {
        let mut tr1 = s.f(0);
        let mut trc = s.f(0);
        let mut t3 = s.f(0);
        for k in 0..tw.tabs[n].len() {
            let d = tw.tabs[n][k].len();
            let ops = &tw.ops[n][k];
            for i in 0..n - 1 {
                let mut s2 = identity_rows(d, p);
                mat_apply(&mut s2, &ops[i], &sig, p);
                mat_apply(&mut s2, &ops[i], &sig, p);
                let mut rhs = identity_rows(d, p);
                mat_apply(&mut rhs, &ops[i], &hplus1, p);
                bump(&mut worst, max_diff(&s2, &rhs, p));
            }
            for i in 0..n.saturating_sub(2) {
                let mut l = identity_rows(d, p);
                for &ii in &[i, i + 1, i] {
                    mat_apply(&mut l, &ops[ii], &sig, p);
                }
                let mut r = identity_rows(d, p);
                for &ii in &[i + 1, i, i + 1] {
                    mat_apply(&mut r, &ops[ii], &sig, p);
                }
                bump(&mut worst, max_diff(&l, &r, p));
            }
            let w = s.weight(n, k);
            tr1 += Float::with_val(p, &w * d as u32);
            let mut mc = identity_rows(d, p);
            for i in 0..n - 1 {
                mat_apply(&mut mc, &ops[i], &sig, p);
            }
            trc += Float::with_val(p, &w * diag_sum(&mc, p));
            if n >= 3 {
                let mut m3 = identity_rows(d, p);
                for &ii in &[0usize, 1, 0] {
                    mat_apply(&mut m3, &ops[ii], &sig, p);
                }
                t3 += Float::with_val(p, &w * diag_sum(&m3, p));
            }
        }
        bump(&mut worst, Float::with_val(p, tr1 - 1u32).abs());
        let zn = Float::with_val(p, (&s.z_d).pow((n - 1) as u32));
        bump(&mut worst, Float::with_val(p, trc - zn).abs());
        if n >= 3 {
            let z2 = Float::with_val(p, &s.z_d * &s.z_d);
            let target = Float::with_val(p, Float::with_val(p, &s.h * &z2) + &s.z_d);
            bump(&mut worst, Float::with_val(p, t3 - target).abs());
        }
    }
    if tw.tabs.len() > 9 {
        let dir = chain_direct_prec(3, 6, p, tw, false);
        let peeled = chain_prec(3, 6, p, tw, false);
        for (a, b) in dir.iter().zip(&peeled) {
            bump(&mut worst, Float::with_val(p, &a.val - &b.val).abs());
        }
    }
    worst
}

// ---------------------------------------------------------------- the walk

/// coefs[strand m][i] index into the three factor types: 0 pp, 1 nn, 2 pn
fn factor_type(ti: bool, tk: bool) -> usize {
    // true = proton
    match (ti, tk) {
        (true, true) => 0,
        (false, false) => 1,
        _ => 2,
    }
}

struct Walk<'a> {
    tw: &'a Tower,
    coefs: [Coefs; 3],
    is_p: Vec<bool>,
    amax: usize,
    prec: u32,
}

/// per-level, per-shape accumulated diagonal sums
type Acc = Vec<Vec<Float>>;

fn new_acc(tw: &Tower, amax: usize, prec: u32) -> Acc {
    (0..=amax)
        .map(|m| (0..tw.tabs[m].len()).map(|_| Float::with_val(prec, 0u32)).collect())
        .collect()
}

impl<'a> Walk<'a> {
    /// child row: lift `row` (level m, shape k) into level m+1 shape k+x, then
    /// multiply by rho(B_m).  Writes into `out` (resized to the child dim).
    fn step(&self, m: usize, k: usize, x: usize, row: &[Float], out: &mut Vec<Float>,
            t1: &mut Float, t2: &mut Float, t3: &mut Float) {
        let kc = k + x;
        let d = self.tw.tabs[m + 1][kc].len();
        if out.len() < d {
            out.resize_with(d, || Float::new(self.prec));
        }
        for v in out[..d].iter_mut() {
            v.assign(0u32);
        }
        for &(j, pj) in &self.tw.embed[m + 1][kc][x] {
            out[j].assign(&row[pj]);
        }
        // strand index m is the new strand; factors i = 0..m-1
        let tk = self.is_p[m];
        for i in 0..m {
            let c = &self.coefs[factor_type(self.is_p[i], tk)];
            apply(&mut out[..d], &self.tw.ops[m + 1][kc][i], c, t1, t2, t3);
        }
    }

    /// DFS from node (m, k, idx) whose row is bufs[m]; accumulate diag entries
    /// at levels >= min_acc; do not descend below level max_level.
    fn dfs(&self, m: usize, k: usize, idx: usize, bufs: &mut [Vec<Float>], acc: &mut Acc,
           min_acc: usize, max_level: usize, t1: &mut Float, t2: &mut Float, t3: &mut Float) {
        if m >= min_acc {
            acc[m][k] += &bufs[m][idx];
        }
        if m >= max_level {
            return;
        }
        for x in 0..2 {
            let ci = self.tw.child[m][k][idx][x];
            if ci == usize::MAX {
                continue;
            }
            let (lo, hi) = bufs.split_at_mut(m + 1);
            self.step(m, k, x, &lo[m], &mut hi[0], t1, t2, t3);
            self.dfs(m + 1, k + x, ci, bufs, acc, min_acc, max_level, t1, t2, t3);
        }
    }

    /// Build the row of an arbitrary node by walking its root path.
    fn path_row(&self, m: usize, k: usize, idx: usize, bufs: &mut [Vec<Float>],
                t1: &mut Float, t2: &mut Float, t3: &mut Float) {
        // reconstruct path upward
        let mut path = Vec::new(); // (level, shape, idx, last) from m down to 2
        let (mut mm, mut kk, mut ii) = (m, k, idx);
        while mm > 1 {
            let (pidx, last) = self.tw.parent[mm][kk][ii];
            path.push((mm, kk, ii, last as usize));
            kk -= last as usize;
            ii = pidx;
            mm -= 1;
        }
        bufs[1].clear();
        bufs[1].push(Float::with_val(self.prec, 1u32));
        for &(lvl, sk, _, last) in path.iter().rev() {
            let (lo, hi) = bufs.split_at_mut(lvl);
            self.step(lvl - 1, sk - last, last, &lo[lvl - 1], &mut hi[0], t1, t2, t3);
        }
    }

    fn run(&self, verbose: bool, tag: &str) -> Acc {
        let amax = self.amax;
        let prec = self.prec;
        let tw = self.tw;
        // split depth: first level with >= 400 nodes (or amax)
        let mut split = 1;
        while split < amax {
            let cnt: usize = tw.tabs[split].iter().map(|v| v.len()).sum();
            if cnt >= 400 {
                break;
            }
            split += 1;
        }
        let mut bufs: Vec<Vec<Float>> = vec![Vec::new(); amax + 1];
        bufs[1].push(Float::with_val(prec, 1u32));
        let mut t1 = Float::new(prec);
        let mut t2 = Float::new(prec);
        let mut t3 = Float::new(prec);
        // levels < split, serially
        let mut acc = new_acc(tw, amax, prec);
        self.dfs(1, 0, 0, &mut bufs, &mut acc, 1, split - 1, &mut t1, &mut t2, &mut t3);
        if split > amax || split - 1 >= amax {
            return acc;
        }
        let tasks: Vec<(usize, usize)> = (0..tw.tabs[split].len())
            .flat_map(|k| (0..tw.tabs[split][k].len()).map(move |j| (k, j)))
            .collect();
        let ntask = tasks.len();
        let done = AtomicUsize::new(0);
        let t0 = Instant::now();
        let last = Mutex::new(Instant::now());
        let partials: Vec<Acc> = tasks
            .par_iter()
            .map(|&(k, j)| {
                let mut bufs: Vec<Vec<Float>> = vec![Vec::new(); amax + 1];
                let mut t1 = Float::new(prec);
                let mut t2 = Float::new(prec);
                let mut t3 = Float::new(prec);
                let mut acc = new_acc(tw, amax, prec);
                self.path_row(split, k, j, &mut bufs, &mut t1, &mut t2, &mut t3);
                self.dfs(split, k, j, &mut bufs, &mut acc, split, amax, &mut t1, &mut t2, &mut t3);
                let n = done.fetch_add(1, Ordering::SeqCst) + 1;
                if verbose {
                    let mut l = last.lock().unwrap();
                    if l.elapsed().as_secs() >= 10 || n == ntask {
                        let el = t0.elapsed().as_secs();
                        let eta = if n > 0 { el * (ntask - n) as u64 / n as u64 } else { 0 };
                        eprintln!("  [{tag}] subtrees {n}/{ntask}  elapsed {el}s  ETA ~{eta}s");
                        *l = Instant::now();
                    }
                }
                acc
            })
            .collect();
        for p in partials {
            for m in 0..=amax {
                for k in 0..acc[m].len() {
                    acc[m][k] += &p[m][k];
                }
            }
        }
        acc
    }
}

struct Row {
    z: usize,
    n: usize,
    a: usize,
    pn: usize,
    val: Float,
}

fn chain_direct_prec(z: usize, nmax: usize, prec: u32, tw: &Tower, verbose: bool) -> Vec<Row> {
    let s = Scalars::new(prec);
    let amax = z + nmax;
    let zero = s.f(0);
    let one = s.f(1);
    let two = s.f(2);
    let mh = Float::with_val(prec, -&s.h);
    let coefs = [
        Coefs::new(&s, &zero, &one, amax),
        Coefs::new(&s, &mh, &one, amax),
        Coefs::new(&s, &mh, &two, amax),
    ];
    let is_p: Vec<bool> = (0..amax).map(|i| i < z).collect();
    let w = Walk { tw, coefs, is_p, amax, prec };
    let acc = w.run(verbose, &format!("Z={z} N<={nmax} prec={prec}"));
    let mut rows = Vec::new();
    for m in (z + 1)..=amax {
        let mut tr = s.f(0);
        for k in 0..tw.tabs[m].len() {
            tr += Float::with_val(prec, s.weight(m, k) * &acc[m][k]);
        }
        let np = z.min(m);
        let nn = m - np;
        let pn = np * nn;
        let two_pn = Float::with_val(prec, s.f(2).pow(pn as u32));
        rows.push(Row { z, n: m - z, a: m, pn, val: tr / two_pn });
    }
    rows
}

// ---------------------------------------------------------------- exact Hecke-Markov peeling

/// Formal generators for the neutron chain over H_{Z+1}(q):
/// - `Q0` = E_{Z,0} * P_Z in H_{Z+1}(q),
/// - `Q`  = P_Z = prod_{i=0}^{Z-1} (2 sigma_i - h) in H_{Z+1}(q),
/// - `S(r)` = sigma_{Z+r} - h = sigma_{Z+r}^{-1} (r >= 0).
/// Every `S(r)` with r >= 1 commutes elementwise with H_{Z+1}(q) (`Q0` and `Q`).
/// By cyclicity of tr_D, the Markov property tr_D(A S(m) B) = (z_D - h) tr_D(A B)
/// for A, B in H_{Z+m+1}(q), and the Hecke/braid relations on {S(r)}, a chain of N
/// neutrons reduces exactly from level Z + N to level Z + floor(N/2) + 1.
#[derive(Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
enum Sym {
    Q0,
    Q,
    S(usize),
}

fn comm_sym(a: Sym, b: Sym) -> bool {
    match (a, b) {
        (Sym::Q0 | Sym::Q, Sym::Q0 | Sym::Q) => false,
        (Sym::Q0 | Sym::Q, Sym::S(r)) | (Sym::S(r), Sym::Q0 | Sym::Q) => r >= 1,
        (Sym::S(x), Sym::S(y)) => x.abs_diff(y) >= 2,
    }
}

fn canon_rotate(wd: &[Sym]) -> Vec<Sym> {
    let i0 = wd.iter().position(|&x| x == Sym::Q0).expect("Q0 present once");
    let mut arr = Vec::with_capacity(wd.len());
    arr.extend_from_slice(&wd[i0..]);
    arr.extend_from_slice(&wd[..i0]);
    loop {
        let mut changed = false;
        for i in 1..arr.len().saturating_sub(1) {
            if comm_sym(arr[i], arr[i + 1]) && arr[i] > arr[i + 1] {
                arr.swap(i, i + 1);
                changed = true;
            }
        }
        if !changed {
            break;
        }
    }
    arr
}

fn add_sym_term(map: &mut BTreeMap<Vec<Sym>, Float>, k: Vec<Sym>, delta: Float) {
    if delta.is_zero() {
        return;
    }
    if let Some(v) = map.get_mut(&k) {
        *v += &delta;
        if v.is_zero() {
            map.remove(&k);
        }
    } else {
        map.insert(k, delta);
    }
}

/// Returns `(lvl_offset, terms)` where evaluation runs in H_{Z + lvl_offset}(q).
fn peel_neutron_word(n_neu: usize, s: &Scalars) -> (usize, Vec<(Vec<Sym>, Float)>) {
    assert!(n_neu >= 1);
    let p = s.prec;
    let mut w = Vec::new();
    for j in 0..n_neu {
        w.push(if j == 0 { Sym::Q0 } else { Sym::Q });
        for r in 0..j {
            w.push(Sym::S(r));
        }
    }
    if n_neu == 1 {
        return (1, vec![(w, s.f(1))]);
    }
    let w_val = Float::with_val(p, &s.z_d - &s.h);
    let mh = Float::with_val(p, -&s.h);
    let mut terms: BTreeMap<Vec<Sym>, Float> = BTreeMap::new();
    terms.insert(canon_rotate(&w), s.f(1));
    let mut cur_max_s: isize = (n_neu as isize) - 2;

    for m in (1..=(n_neu - 2)).rev() {
        let target = Sym::S(m);
        let mut ok = true;
        let mut nxt: BTreeMap<Vec<Sym>, Float> = BTreeMap::new();
        let mut stack: Vec<(Vec<Sym>, Float)> = terms.iter().map(|(k, v)| (k.clone(), v.clone())).collect();
        let mut steps = 0usize;
        while let Some((wd, cf)) = stack.pop() {
            steps += 1;
            if steps > 50_000 {
                ok = false;
                break;
            }
            if cf.is_zero() {
                continue;
            }
            let cnt = wd.iter().filter(|&&x| x == target).count();
            if cnt == 0 {
                add_sym_term(&mut nxt, canon_rotate(&wd), cf);
                continue;
            }
            if cnt == 1 {
                let pos = wd.iter().position(|&x| x == target).unwrap();
                let mut nw = Vec::with_capacity(wd.len() - 1);
                nw.extend_from_slice(&wd[..pos]);
                nw.extend_from_slice(&wd[pos + 1..]);
                add_sym_term(&mut nxt, canon_rotate(&nw), Float::with_val(p, &cf * &w_val));
                continue;
            }
            let idxs: Vec<usize> = wd
                .iter()
                .enumerate()
                .filter_map(|(i, &x)| if x == target { Some(i) } else { None })
                .collect();
            let mut reduced = false;
            for idx_pos in 0..idxs.len() {
                let a = idxs[idx_pos];
                let mut wk = Vec::with_capacity(wd.len());
                wk.extend_from_slice(&wd[a..]);
                wk.extend_from_slice(&wd[..a]);
                let b = (idxs[(idx_pos + 1) % idxs.len()] + wd.len() - a) % wd.len();
                let seg = &wk[1..b];
                let mut l = 0usize;
                while l < seg.len() && comm_sym(seg[l], target) {
                    l += 1;
                }
                let mut r = seg.len();
                while r > l && comm_sym(seg[r - 1], target) {
                    r -= 1;
                }
                let mid = &seg[l..r];
                let pref = &seg[..l];
                let suf = &seg[r..];
                let rest = &wk[b + 1..];
                if mid.is_empty() {
                    let mut w1 = Vec::with_capacity(wk.len() - 2);
                    w1.extend_from_slice(pref);
                    w1.extend_from_slice(suf);
                    w1.extend_from_slice(rest);
                    let mut w2 = Vec::with_capacity(wk.len() - 1);
                    w2.extend_from_slice(pref);
                    w2.push(target);
                    w2.extend_from_slice(suf);
                    w2.extend_from_slice(rest);
                    stack.push((w1, cf.clone()));
                    stack.push((w2, Float::with_val(p, &mh * &cf)));
                    reduced = true;
                    break;
                } else if mid.len() == 1 && mid[0] == Sym::S(m - 1) {
                    let mut nw = Vec::with_capacity(wk.len());
                    nw.extend_from_slice(pref);
                    nw.push(Sym::S(m - 1));
                    nw.push(target);
                    nw.push(Sym::S(m - 1));
                    nw.extend_from_slice(suf);
                    nw.extend_from_slice(rest);
                    stack.push((nw, cf));
                    reduced = true;
                    break;
                } else {
                    let mut simp = false;
                    for pos in 0..mid.len() {
                        if comm_sym(mid[pos], target) && (0..pos).all(|u| comm_sym(mid[u], mid[pos])) {
                            let mut nw = Vec::with_capacity(wk.len());
                            nw.push(target);
                            nw.extend_from_slice(pref);
                            nw.push(mid[pos]);
                            nw.extend_from_slice(&mid[..pos]);
                            nw.extend_from_slice(&mid[pos + 1..]);
                            nw.extend_from_slice(suf);
                            nw.push(target);
                            nw.extend_from_slice(rest);
                            stack.push((nw, cf.clone()));
                            simp = true;
                            break;
                        }
                        if comm_sym(mid[pos], target)
                            && ((pos + 1)..mid.len()).all(|u| comm_sym(mid[pos], mid[u]))
                        {
                            let mut nw = Vec::with_capacity(wk.len());
                            nw.push(target);
                            nw.extend_from_slice(pref);
                            nw.extend_from_slice(&mid[..pos]);
                            nw.extend_from_slice(&mid[pos + 1..]);
                            nw.push(mid[pos]);
                            nw.extend_from_slice(suf);
                            nw.push(target);
                            nw.extend_from_slice(rest);
                            stack.push((nw, cf.clone()));
                            simp = true;
                            break;
                        }
                    }
                    if simp {
                        reduced = true;
                        break;
                    }
                    for p1 in 0..mid.len() {
                        let Sym::S(k) = mid[p1] else { continue };
                        for p2 in (p1 + 1)..mid.len() {
                            if mid[p2] != Sym::S(k) {
                                continue;
                            }
                            let sub = &mid[p1 + 1..p2];
                            if sub.iter().all(|&u| comm_sym(u, Sym::S(k))) {
                                let mut w1 = Vec::with_capacity(wk.len() - 2);
                                w1.push(target);
                                w1.extend_from_slice(pref);
                                w1.extend_from_slice(&mid[..p1]);
                                w1.extend_from_slice(sub);
                                w1.extend_from_slice(&mid[p2 + 1..]);
                                w1.extend_from_slice(suf);
                                w1.push(target);
                                w1.extend_from_slice(rest);

                                let mut w2 = Vec::with_capacity(wk.len() - 1);
                                w2.push(target);
                                w2.extend_from_slice(pref);
                                w2.extend_from_slice(&mid[..p1]);
                                w2.extend_from_slice(sub);
                                w2.push(Sym::S(k));
                                w2.extend_from_slice(&mid[p2 + 1..]);
                                w2.extend_from_slice(suf);
                                w2.push(target);
                                w2.extend_from_slice(rest);

                                stack.push((w1, cf.clone()));
                                stack.push((w2, Float::with_val(p, &mh * &cf)));
                                simp = true;
                                break;
                            }
                            let non_comm: Vec<usize> = sub
                                .iter()
                                .enumerate()
                                .filter_map(|(ix, &u)| if !comm_sym(u, Sym::S(k)) { Some(ix) } else { None })
                                .collect();
                            if non_comm.len() == 1 && k >= 1 && sub[non_comm[0]] == Sym::S(k - 1) {
                                let c_idx = non_comm[0];
                                let mut nw = Vec::with_capacity(wk.len());
                                nw.push(target);
                                nw.extend_from_slice(pref);
                                nw.extend_from_slice(&mid[..p1]);
                                nw.extend_from_slice(&sub[..c_idx]);
                                nw.push(Sym::S(k - 1));
                                nw.push(Sym::S(k));
                                nw.push(Sym::S(k - 1));
                                nw.extend_from_slice(&sub[c_idx + 1..]);
                                nw.extend_from_slice(&mid[p2 + 1..]);
                                nw.extend_from_slice(suf);
                                nw.push(target);
                                nw.extend_from_slice(rest);
                                stack.push((nw, cf.clone()));
                                simp = true;
                                break;
                            }
                        }
                        if simp {
                            break;
                        }
                    }
                    if simp {
                        reduced = true;
                        break;
                    }
                }
            }
            if !reduced {
                ok = false;
                break;
            }
        }
        if !ok {
            break;
        }
        terms = nxt;
        cur_max_s = (m as isize) - 1;
    }
    let lvl_off = if cur_max_s < 0 { 1 } else { (cur_max_s as usize) + 2 };
    (lvl_off, terms.into_iter().collect())
}

struct TrieNode {
    edges: Vec<(Sym, usize)>,
}

struct WalkPeel<'a> {
    tw: &'a Tower,
    coefs: [Coefs; 3],
    z: usize,
    lvl: usize,
    prec: u32,
    trie: Vec<TrieNode>,
    max_depth: usize,
}

impl<'a> WalkPeel<'a> {
    /// Lift `row` (level m, shape k) into level m+1 shape k+x; apply proton/first-neutron
    /// factors only for m <= z (producing Q0 at level z+1, then pure GT lift to `lvl`).
    fn step_lift(
        &self,
        m: usize,
        k: usize,
        x: usize,
        row: &[Float],
        out: &mut Vec<Float>,
        t1: &mut Float,
        t2: &mut Float,
        t3: &mut Float,
    ) {
        let kc = k + x;
        let d = self.tw.tabs[m + 1][kc].len();
        if out.len() < d {
            out.resize_with(d, || Float::new(self.prec));
        }
        for v in out[..d].iter_mut() {
            v.assign(0u32);
        }
        for &(j, pj) in &self.tw.embed[m + 1][kc][x] {
            out[j].assign(&row[pj]);
        }
        if m < self.z {
            for i in 0..m {
                apply(&mut out[..d], &self.tw.ops[m + 1][kc][i], &self.coefs[0], t1, t2, t3);
            }
        } else if m == self.z {
            for i in 0..self.z {
                apply(&mut out[..d], &self.tw.ops[m + 1][kc][i], &self.coefs[2], t1, t2, t3);
            }
        }
    }

    fn eval_trie(
        &self,
        u: usize,
        dep: usize,
        k: usize,
        idx: usize,
        d: usize,
        tbufs: &mut [Vec<Float>],
        node_acc: &mut [Vec<Float>],
        t1: &mut Float,
        t2: &mut Float,
        t3: &mut Float,
    ) {
        node_acc[u][k] += &tbufs[dep][idx];
        for &(sym, child_u) in &self.trie[u].edges {
            let (lo, hi) = tbufs.split_at_mut(dep + 1);
            let cur = &lo[dep][..d];
            let nxt = &mut hi[0];
            if nxt.len() < d {
                nxt.resize_with(d, || Float::new(self.prec));
            }
            for j in 0..d {
                nxt[j].assign(&cur[j]);
            }
            match sym {
                Sym::Q => {
                    for i in 0..self.z {
                        apply(&mut nxt[..d], &self.tw.ops[self.lvl][k][i], &self.coefs[2], t1, t2, t3);
                    }
                }
                Sym::S(r) => {
                    apply(&mut nxt[..d], &self.tw.ops[self.lvl][k][self.z + r], &self.coefs[1], t1, t2, t3);
                }
                Sym::Q0 => unreachable!("Q0 only at root"),
            }
            self.eval_trie(child_u, dep + 1, k, idx, d, tbufs, node_acc, t1, t2, t3);
        }
    }

    fn dfs_peel(
        &self,
        m: usize,
        k: usize,
        idx: usize,
        bufs: &mut [Vec<Float>],
        tbufs: &mut [Vec<Float>],
        node_acc: &mut [Vec<Float>],
        t1: &mut Float,
        t2: &mut Float,
        t3: &mut Float,
    ) {
        if m == self.lvl {
            let d = self.tw.tabs[self.lvl][k].len();
            if tbufs[0].len() < d {
                tbufs[0].resize_with(d, || Float::new(self.prec));
            }
            for j in 0..d {
                tbufs[0][j].assign(&bufs[self.lvl][j]);
            }
            self.eval_trie(0, 0, k, idx, d, tbufs, node_acc, t1, t2, t3);
            return;
        }
        for x in 0..2 {
            let ci = self.tw.child[m][k][idx][x];
            if ci == usize::MAX {
                continue;
            }
            let (lo, hi) = bufs.split_at_mut(m + 1);
            self.step_lift(m, k, x, &lo[m], &mut hi[0], t1, t2, t3);
            self.dfs_peel(m + 1, k + x, ci, bufs, tbufs, node_acc, t1, t2, t3);
        }
    }

    fn path_row(
        &self,
        m: usize,
        k: usize,
        idx: usize,
        bufs: &mut [Vec<Float>],
        t1: &mut Float,
        t2: &mut Float,
        t3: &mut Float,
    ) {
        let mut path = Vec::new();
        let (mut mm, mut kk, mut ii) = (m, k, idx);
        while mm > 1 {
            let (pidx, last) = self.tw.parent[mm][kk][ii];
            path.push((mm, kk, ii, last as usize));
            kk -= last as usize;
            ii = pidx;
            mm -= 1;
        }
        bufs[1].clear();
        bufs[1].push(Float::with_val(self.prec, 1u32));
        for &(lv, sk, _, last) in path.iter().rev() {
            let (lo, hi) = bufs.split_at_mut(lv);
            self.step_lift(lv - 1, sk - last, last, &lo[lv - 1], &mut hi[0], t1, t2, t3);
        }
    }

    fn new_node_acc(&self) -> Vec<Vec<Float>> {
        let n_shapes = self.tw.tabs[self.lvl].len();
        (0..self.trie.len())
            .map(|_| (0..n_shapes).map(|_| Float::with_val(self.prec, 0u32)).collect())
            .collect()
    }

    fn run(&self, verbose: bool, tag: &str) -> Vec<Vec<Float>> {
        let lvl = self.lvl;
        let prec = self.prec;
        let tw = self.tw;
        let mut split = 1;
        while split < lvl {
            let cnt: usize = tw.tabs[split].iter().map(|v| v.len()).sum();
            if cnt >= 400 {
                break;
            }
            split += 1;
        }
        if split >= lvl {
            let mut bufs: Vec<Vec<Float>> = vec![Vec::new(); lvl + 1];
            bufs[1].push(Float::with_val(prec, 1u32));
            let mut tbufs: Vec<Vec<Float>> = vec![Vec::new(); self.max_depth + 2];
            let mut t1 = Float::new(prec);
            let mut t2 = Float::new(prec);
            let mut t3 = Float::new(prec);
            let mut node_acc = self.new_node_acc();
            self.dfs_peel(1, 0, 0, &mut bufs, &mut tbufs, &mut node_acc, &mut t1, &mut t2, &mut t3);
            return node_acc;
        }
        let tasks: Vec<(usize, usize)> = (0..tw.tabs[split].len())
            .flat_map(|k| (0..tw.tabs[split][k].len()).map(move |j| (k, j)))
            .collect();
        let ntask = tasks.len();
        let done = AtomicUsize::new(0);
        let t0 = Instant::now();
        let last = Mutex::new(Instant::now());
        let partials: Vec<Vec<Vec<Float>>> = tasks
            .par_iter()
            .map(|&(k, j)| {
                let mut bufs: Vec<Vec<Float>> = vec![Vec::new(); lvl + 1];
                let mut tbufs: Vec<Vec<Float>> = vec![Vec::new(); self.max_depth + 2];
                let mut t1 = Float::new(prec);
                let mut t2 = Float::new(prec);
                let mut t3 = Float::new(prec);
                let mut node_acc = self.new_node_acc();
                self.path_row(split, k, j, &mut bufs, &mut t1, &mut t2, &mut t3);
                self.dfs_peel(split, k, j, &mut bufs, &mut tbufs, &mut node_acc, &mut t1, &mut t2, &mut t3);
                let n = done.fetch_add(1, Ordering::SeqCst) + 1;
                if verbose {
                    let mut l = last.lock().unwrap();
                    if l.elapsed().as_secs() >= 10 || n == ntask {
                        let el = t0.elapsed().as_secs();
                        let eta = if n > 0 { el * (ntask - n) as u64 / n as u64 } else { 0 };
                        eprintln!("  [{tag}] subtrees {n}/{ntask}  elapsed {el}s  ETA ~{eta}s");
                        *l = Instant::now();
                    }
                }
                node_acc
            })
            .collect();
        let mut out = self.new_node_acc();
        for p in partials {
            for u in 0..out.len() {
                for k in 0..out[u].len() {
                    out[u][k] += &p[u][k];
                }
            }
        }
        out
    }
}

fn chain_prec(z: usize, nmax: usize, prec: u32, tw: &Tower, verbose: bool) -> Vec<Row> {
    let s = Scalars::new(prec);
    let zero = s.f(0);
    let one = s.f(1);
    let two = s.f(2);
    let mh = Float::with_val(prec, -&s.h);

    // Group n = 1..=nmax by reduced evaluation level `lvl = z + lvl_off`.
    let mut by_lvl: BTreeMap<usize, Vec<(usize, Vec<(Vec<Sym>, Float)>)>> = BTreeMap::new();
    for n in 1..=nmax {
        let (lvl_off, terms) = peel_neutron_word(n, &s);
        by_lvl.entry(z + lvl_off).or_default().push((n, terms));
    }

    let mut val_by_n: BTreeMap<usize, Float> = BTreeMap::new();
    for (lvl, group) in by_lvl {
        let mut trie = vec![TrieNode { edges: Vec::new() }];
        let mut max_depth = 0usize;
        // (n_neu, trie_node_index, coeff)
        let mut terminals: Vec<(usize, usize, Float)> = Vec::new();
        for (n_neu, terms) in group {
            for (wd, cf) in terms {
                assert_eq!(wd[0], Sym::Q0);
                let tail = &wd[1..];
                if tail.len() > max_depth {
                    max_depth = tail.len();
                }
                let mut u = 0usize;
                for &sym in tail {
                    if let Some(&(_, nxt_u)) = trie[u].edges.iter().find(|&&(es, _)| es == sym) {
                        u = nxt_u;
                    } else {
                        let nxt_u = trie.len();
                        trie.push(TrieNode { edges: Vec::new() });
                        trie[u].edges.push((sym, nxt_u));
                        u = nxt_u;
                    }
                }
                terminals.push((n_neu, u, cf));
            }
        }
        let coefs = [
            Coefs::new(&s, &zero, &one, lvl),
            Coefs::new(&s, &mh, &one, lvl),
            Coefs::new(&s, &mh, &two, lvl),
        ];
        let wp = WalkPeel { tw, coefs, z, lvl, prec, trie, max_depth };
        let node_acc = wp.run(verbose, &format!("Z={z} lvl={lvl} prec={prec}"));
        let weights: Vec<Float> = (0..tw.tabs[lvl].len()).map(|k| s.weight(lvl, k)).collect();
        let node_tr: Vec<Float> = node_acc
            .iter()
            .map(|per_k| {
                let mut tr = s.f(0);
                for (k, v) in per_k.iter().enumerate() {
                    tr += Float::with_val(prec, &weights[k] * v);
                }
                tr
            })
            .collect();
        for (n_neu, u, cf) in terminals {
            let e = val_by_n.entry(n_neu).or_insert_with(|| s.f(0));
            *e += Float::with_val(prec, &cf * &node_tr[u]);
        }
    }

    let mut rows = Vec::new();
    for n in 1..=nmax {
        let a = z + n;
        let pn = z * n;
        let two_pn = Float::with_val(prec, s.f(2).pow(pn as u32));
        let tr = val_by_n.remove(&n).expect("computed n");
        rows.push(Row { z, n, a, pn, val: tr / two_pn });
    }
    rows
}

fn chain(z: usize, nmax: usize, dps: u32, tw: &Tower, verbose: bool) -> Vec<Row> {
    chain_prec(z, nmax, bits_for(dps), tw, verbose)
}

// ---------------------------------------------------------------- output

/// mpmath-nstr-like rendering with `n` significant digits.
fn nstr(x: &Float, n: usize) -> String {
    if x.is_zero() {
        return "0.0".into();
    }
    let (neg, digits, exp) = x.to_sign_string_exp(10, Some(n));
    let exp = exp.expect("finite");
    let digits = digits.trim_end_matches('0').to_string();
    let digits = if digits.is_empty() { "0".to_string() } else { digits };
    // value = 0.digits * 10^exp ; leading digit exponent = exp - 1
    let e = exp as i64 - 1;
    let sign = if neg { "-" } else { "" };
    if e >= -20 && e < n as i64 {
        if exp <= 0 {
            format!("{sign}0.{}{}", "0".repeat((-exp) as usize), digits)
        } else {
            let ex = exp as usize;
            if digits.len() <= ex {
                format!("{sign}{}{}.0", digits, "0".repeat(ex - digits.len()))
            } else {
                format!("{sign}{}.{}", &digits[..ex], &digits[ex..])
            }
        }
    } else {
        let (h, t) = digits.split_at(1);
        let t = if t.is_empty() { "0" } else { t };
        format!("{sign}{h}.{t}e{e}")
    }
}

fn agree_value(a: &Float, b: &Float, prec: u32) -> Option<Float> {
    let d = Float::with_val(prec, a - b).abs();
    if d.is_zero() {
        return None;
    }
    let rel = Float::with_val(prec, &d / Float::with_val(prec, b.abs_ref()));
    Some(Float::with_val(prec, -rel.log10()))
}

fn sym(z: usize) -> &'static str {
    const S: [&str; 21] = ["?", "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na",
                           "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca"];
    S.get(z).copied().unwrap_or("?")
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut chains: Vec<(usize, usize)> = Vec::new();
    let mut dps: u32 = 80;
    let mut check_dps: u32 = 70;
    let mut out: Option<String> = None;
    let mut compare: Option<String> = None;
    let mut from_witness = false;
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--chain" => {
                let v: Vec<usize> = args[i + 1].split(':').map(|x| x.parse().unwrap()).collect();
                chains.push((v[0], v[1]));
                i += 1;
            }
            "--dps" => { dps = args[i + 1].parse().unwrap(); i += 1; }
            "--check-dps" => { check_dps = args[i + 1].parse().unwrap(); i += 1; }
            "--out" => { out = Some(args[i + 1].clone()); i += 1; }
            "--compare" => { compare = Some(args[i + 1].clone()); i += 1; }
            "--chains-from-compare" => { from_witness = true; }
            "-h" | "--help" => {
                eprintln!("hecke-tower-trace --chain Z:Nmax [--chain ...] [--dps 80] [--check-dps 70] \
                           [--compare witness.json [--chains-from-compare]] [--out file.json]");
                return;
            }
            o => panic!("unknown arg {o}"),
        }
        i += 1;
    }
    let reference: Option<Value> = compare.as_ref().map(|p| {
        serde_json::from_str(&std::fs::read_to_string(p).expect("read compare")).expect("json")
    });
    if from_witness {
        let r = reference.as_ref().expect("--chains-from-compare needs --compare");
        let mut mx: HashMap<usize, usize> = HashMap::new();
        for row in r["rows"].as_array().unwrap() {
            let z = row["z"].as_u64().unwrap() as usize;
            let n = row["n"].as_u64().unwrap() as usize;
            let e = mx.entry(z).or_insert(0);
            if n > *e {
                *e = n;
            }
        }
        let mut v: Vec<_> = mx.into_iter().collect();
        v.sort();
        chains.extend(v);
    }
    assert!(!chains.is_empty(), "give --chain Z:N");
    assert!(dps >= 80, "working precision must be >= 80 decimal digits");
    assert!(check_dps >= 65 && check_dps != dps, "check precision must be >= 65 and differ");
    let amax = chains.iter().map(|&(z, n)| z + n).max().unwrap();
    assert!(amax <= 31, "bitmask tableaux support A <= 31");
    let s_lvl = Scalars::new(bits_for(dps));
    let lvl_max = chains
        .iter()
        .flat_map(|&(z, nmax)| {
            let s_ref = &s_lvl;
            (1..=nmax).map(move |n| z + peel_neutron_word(n, s_ref).0)
        })
        .max()
        .unwrap()
        .max(9);
    let t_start = Instant::now();
    let tw = Tower::new(lvl_max);
    eprintln!("tower built to level {} (peeled from A_max={}) in {:.1?}; largest dim at level {}: {}",
              lvl_max, amax, t_start.elapsed(), lvl_max,
              tw.tabs[lvl_max].iter().map(|v| v.len()).max().unwrap());

    // self-checks at both precisions, failing hard
    let mut checks = Vec::new();
    for &d in &[dps, check_dps] {
        let s = Scalars::new(bits_for(d));
        let worst = self_check(&s, &tw, 8);
        let tol = Float::with_val(bits_for(d), Float::with_val(bits_for(d), 10u32).pow(-((d as i32) - 15)));
        eprintln!("self-check dps={d} (Hecke, braid, tr(1), Markov z^(n-1), s0s1s0) n<=8: worst {}",
                  nstr(&Float::with_val(64, &worst), 4));
        if !(worst < tol) {
            eprintln!("SELF-CHECK FAILED");
            std::process::exit(2);
        }
        checks.push(json!({"dps": d, "nmax": 8, "worst_residual": nstr(&Float::with_val(64, &worst), 5)}));
    }

    let mut rows_json = Vec::new();
    let mut timings = Vec::new();
    let mut min_prec_agree: Option<Float> = None;
    let mut min_ref_agree: Option<Float> = None;
    let mut ref_compared = 0usize;
    let mut ref_missing = Vec::new();
    let ref_map: HashMap<(u64, u64), String> = reference
        .as_ref()
        .map(|r| {
            r["rows"].as_array().unwrap().iter()
                .map(|row| ((row["z"].as_u64().unwrap(), row["n"].as_u64().unwrap()),
                            row["tr_markov_d"].as_str().unwrap().to_string()))
                .collect()
        })
        .unwrap_or_default();
    let cmp_prec = bits_for(dps);
    for &(z, nmax) in &chains {
        let t0 = Instant::now();
        let main_rows = chain(z, nmax, dps, &tw, true);
        let t_main = t0.elapsed();
        let t1 = Instant::now();
        let chk_rows = chain(z, nmax, check_dps, &tw, true);
        let t_chk = t1.elapsed();
        eprintln!("chain Z={z} N<={nmax} (A<={}): dps {dps} {:.2?}, dps {check_dps} {:.2?}",
                  z + nmax, t_main, t_chk);
        timings.push(json!({"z": z, "n_max": nmax, "a_max": z + nmax,
                            "seconds_main_dps": t_main.as_secs_f64_free().to_string(),
                            "seconds_check_dps": t_chk.as_secs_f64_free().to_string()}));
        for (r, c) in main_rows.iter().zip(&chk_rows) {
            let pa = agree_value(&r.val, &c.val, cmp_prec);
            if let Some(ref v) = pa {
                if min_prec_agree.as_ref().map(|m| v < m).unwrap_or(true) {
                    min_prec_agree = Some(v.clone());
                }
            }
            let prec_s = pa.as_ref().map(|v| nstr(&Float::with_val(32, v), 4))
                .unwrap_or_else(|| "exact".into());
            let mut row = json!({
                "isotope": format!("{}{}", r.a, sym(z)), "z": r.z, "n": r.n, "a": r.a,
                "pn": r.pn, "tr_markov_d": nstr(&r.val, 60),
                "two_precision_agreement_digits": prec_s,
            });
            if let Some(s) = ref_map.get(&(z as u64, r.n as u64)) {
                let refv = Float::with_val(cmp_prec, Float::parse(s).expect("ref parses"));
                let ra = agree_value(&r.val, &refv, cmp_prec);
                if let Some(ref v) = ra {
                    if min_ref_agree.as_ref().map(|m| v < m).unwrap_or(true) {
                        min_ref_agree = Some(v.clone());
                    }
                }
                ref_compared += 1;
                row["python_reference_agreement_digits"] = json!(ra.as_ref()
                    .map(|v| nstr(&Float::with_val(32, v), 4)).unwrap_or_else(|| "exact".into()));
            } else if reference.is_some() {
                ref_missing.push(format!("{}{}", r.a, sym(z)));
            }
            eprintln!("  {:>5} pn={:<3} {}  (prec-agree {})", format!("{}{}", r.a, sym(z)),
                      r.pn, &nstr(&r.val, 40), prec_s);
            rows_json.push(row);
        }
    }
    let fmt = |o: &Option<Float>| o.as_ref().map(|v| nstr(&Float::with_val(32, v), 4))
        .unwrap_or_else(|| "exact".into());
    let ref_total = reference.as_ref().map(|r| r["rows"].as_array().unwrap().len()).unwrap_or(0);
    eprintln!("min two-precision agreement: {} digits", fmt(&min_prec_agree));
    if reference.is_some() {
        eprintln!("python reference: compared {ref_compared}/{ref_total} rows, min agreement {} digits",
                  fmt(&min_ref_agree));
    }
    if let Some(p) = out {
        let w = json!({
            "description": "Convention-D Markov trace of the v9 nuclear element, sum over two-row shapes of [n-2k+1]_q/[2]_q^n times the Young-seminormal character, computed by a depth-first walk over the Gelfand-Tsetlin tableau tree carrying one MPFR row vector per node (diagonal of the tower product only); divided by 2^pn like the v9 certificate field tr_markov_d. Rust port of computations/probes/markov_trace_two_row_tower_probe.py.",
            "producer": "tools/hecke-engine/src/bin/tower_trace.rs",
            "producer_binary": "hecke-tower-trace (cargo build --release --bin hecke-tower-trace --features mpfr)",
            "python_reference_producer": "computations/probes/markov_trace_two_row_tower_probe.py",
            "q0": Q0_STR,
            "q0_anchor": "proton",
            "q0Anchor": "proton",
            "q0Value": Q0_STR,
            "z": "q^3/(q^2+1)",
            "dps": dps,
            "check_dps": check_dps,
            "mpfr_bits": {"main": bits_for(dps), "check": bits_for(check_dps)},
            "self_checks": checks,
            "min_two_precision_agreement_digits": fmt(&min_prec_agree),
            "python_reference": compare.as_ref().map(|c| json!({
                "file": c, "rows_compared": ref_compared, "rows_in_reference": ref_total,
                "min_agreement_digits": fmt(&min_ref_agree),
            })),
            "timings": timings,
            "rows": rows_json,
        });
        std::fs::write(&p, serde_json::to_string_pretty(&w).unwrap() + "\n").expect("write out");
        eprintln!("wrote {p}");
    }
}

/// Display-only duration formatting without f64 arithmetic in results.
trait DurSecs {
    fn as_secs_f64_free(&self) -> Millis;
}
struct Millis(u128);
impl std::fmt::Display for Millis {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}.{:03}", self.0 / 1000, self.0 % 1000)
    }
}
impl DurSecs for std::time::Duration {
    fn as_secs_f64_free(&self) -> Millis {
        Millis(self.as_millis())
    }
}
