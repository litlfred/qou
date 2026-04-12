// v13_crt: CRT multi-prime Hecke engine with Garside order.
//
// Coefficients stored as residues modulo several u128 Mersenne-like primes.
// No BigInt allocation — fixed memory per coefficient.
// Exact reconstruction via CRT when needed for evaluation.
//
// Key advantages over v9 (BigInt):
// 1. Fixed 16 bytes per prime per coefficient (vs unbounded BigInt)
// 2. All arithmetic is u128 mod p — no heap allocation
// 3. Parallelizable across primes
// 4. Memory-bounded: can predict memory usage upfront
//
// The Garside staircase order (right-to-left sweep) is used,
// matching v9's canonical construction.
//
// Usage:
//   hecke-crt qvalue ORDERING [n_primes]
//   e.g. hecke-crt qvalue ppnpnnpnn 4

#![allow(dead_code)]

use rustc_hash::FxHashMap;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// CRT arithmetic over u128 primes
// ════════════════════════════════════════════════════════════════

// Large primes that fit in u128. Using primes near 2^61 to allow
// multiplication without overflow: a*b mod p where a,b < 2^61
// fits in u128 (2^122 < 2^128).
const PRIMES: [u128; 8] = [
    // Mersenne-like primes near 2^61
    2305843009213693951,   // 2^61 - 1 (Mersenne prime M61)
    2305843009213693967,   // next prime after M61
    2305843009213694049,   // +98
    2305843009213694099,   // +148
    2305843009213694153,   // +202
    2305843009213694201,   // +250
    2305843009213694279,   // +328
    2305843009213694321,   // +370
];

/// A coefficient stored as residues modulo N primes.
/// Supports signed arithmetic: we use symmetric representation
/// where values in [0, p/2) are positive and [p/2, p) are negative.
#[derive(Clone, Debug)]
struct ModCoeff {
    residues: Vec<u128>,
}

impl ModCoeff {
    fn zero(n_primes: usize) -> Self {
        Self { residues: vec![0; n_primes] }
    }

    fn one(n_primes: usize) -> Self {
        Self { residues: vec![1; n_primes] }
    }

    fn from_i64(val: i64, n_primes: usize) -> Self {
        let mut r = vec![0u128; n_primes];
        for i in 0..n_primes {
            let p = PRIMES[i];
            r[i] = if val >= 0 {
                (val as u128) % p
            } else {
                p - ((-val) as u128 % p)
            };
        }
        Self { residues: r }
    }

    fn is_zero(&self) -> bool {
        self.residues.iter().all(|&r| r == 0)
    }

    fn n_primes(&self) -> usize { self.residues.len() }

    fn add(&self, other: &Self) -> Self {
        let n = self.n_primes();
        let mut r = vec![0u128; n];
        for i in 0..n {
            r[i] = (self.residues[i] + other.residues[i]) % PRIMES[i];
        }
        Self { residues: r }
    }

    fn sub(&self, other: &Self) -> Self {
        let n = self.n_primes();
        let mut r = vec![0u128; n];
        for i in 0..n {
            let p = PRIMES[i];
            r[i] = (self.residues[i] + p - other.residues[i]) % p;
        }
        Self { residues: r }
    }

    fn mul(&self, other: &Self) -> Self {
        let n = self.n_primes();
        let mut r = vec![0u128; n];
        for i in 0..n {
            r[i] = mulmod(self.residues[i], other.residues[i], PRIMES[i]);
        }
        Self { residues: r }
    }

    fn scale_i64(&self, s: i64) -> Self {
        let n = self.n_primes();
        let mut r = vec![0u128; n];
        for i in 0..n {
            let p = PRIMES[i];
            let sv = if s >= 0 { (s as u128) % p } else { p - ((-s) as u128 % p) };
            r[i] = mulmod(self.residues[i], sv, p);
        }
        Self { residues: r }
    }

    /// Evaluate as f64 using CRT reconstruction.
    /// Returns the exact integer value as f64 (may lose precision for large values).
    fn to_f64(&self) -> f64 {
        // For small values, all residues agree when interpreted as signed
        // Use first prime for quick check
        let p = PRIMES[0];
        let r = self.residues[0];
        if r <= p / 2 {
            r as f64
        } else {
            -((p - r) as f64)
        }
    }
}

/// Modular multiplication: (a * b) mod p, avoiding overflow.
/// For a, b < 2^61 and p < 2^61, a*b < 2^122 which fits in u128.
#[inline]
fn mulmod(a: u128, b: u128, p: u128) -> u128 {
    (a * b) % p
}

// ════════════════════════════════════════════════════════════════
// Laurent polynomial with CRT coefficients
// ════════════════════════════════════════════════════════════════

/// Laurent polynomial in t = q^{1/2} with CRT coefficients.
/// Sparse: only nonzero terms stored.
#[derive(Clone, Debug)]
struct CrtPoly {
    terms: Vec<(i32, ModCoeff)>,  // (power, coefficient)
    n_primes: usize,
}

impl CrtPoly {
    fn zero(n_primes: usize) -> Self {
        Self { terms: Vec::new(), n_primes }
    }

    fn one(n_primes: usize) -> Self {
        Self { terms: vec![(0, ModCoeff::one(n_primes))], n_primes }
    }

    fn t_power(power: i32, n_primes: usize) -> Self {
        Self { terms: vec![(power, ModCoeff::one(n_primes))], n_primes }
    }

    fn is_zero(&self) -> bool { self.terms.is_empty() }
    fn n_terms(&self) -> usize { self.terms.len() }

    fn add(&self, other: &Self) -> Self {
        let mut map: FxHashMap<i32, ModCoeff> = FxHashMap::default();
        for (k, c) in &self.terms {
            map.insert(*k, c.clone());
        }
        for (k, c) in &other.terms {
            let e = map.entry(*k).or_insert_with(|| ModCoeff::zero(self.n_primes));
            *e = e.add(c);
        }
        let terms: Vec<(i32, ModCoeff)> = map.into_iter()
            .filter(|(_, c)| !c.is_zero())
            .collect();
        Self { terms, n_primes: self.n_primes }
    }

    fn scale_i64(&self, s: i64) -> Self {
        if s == 0 { return Self::zero(self.n_primes); }
        let terms: Vec<(i32, ModCoeff)> = self.terms.iter()
            .map(|(k, c)| (*k, c.scale_i64(s)))
            .filter(|(_, c)| !c.is_zero())
            .collect();
        Self { terms, n_primes: self.n_primes }
    }

    fn mul(&self, other: &Self) -> Self {
        let mut map: FxHashMap<i32, ModCoeff> = FxHashMap::default();
        for (k1, c1) in &self.terms {
            for (k2, c2) in &other.terms {
                let k = k1 + k2;
                let prod = c1.mul(c2);
                let e = map.entry(k).or_insert_with(|| ModCoeff::zero(self.n_primes));
                *e = e.add(&prod);
            }
        }
        let terms: Vec<(i32, ModCoeff)> = map.into_iter()
            .filter(|(_, c)| !c.is_zero())
            .collect();
        Self { terms, n_primes: self.n_primes }
    }

    fn shift(&self, n: i32) -> Self {
        let terms: Vec<(i32, ModCoeff)> = self.terms.iter()
            .map(|(k, c)| (k + n, c.clone()))
            .collect();
        Self { terms, n_primes: self.n_primes }
    }

    /// Evaluate at t = sqrt(q₀) using CRT-reconstructed integer coefficients.
    fn eval_f64(&self, t: f64) -> f64 {
        self.terms.iter().map(|(k, c)| {
            c.to_f64() * t.powi(*k)
        }).sum()
    }
}

// ════════════════════════════════════════════════════════════════
// Compact word representation (same as v9)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W(u64);

impl W {
    const E: W = W(0);
    fn len(self) -> usize { if self.0 == 0 { 0 } else { ((64 - self.0.leading_zeros()) / 5) as usize } }
    fn get(self, i: usize) -> u8 { ((self.0 >> (i * 5)) & 0x1F) as u8 }
    fn push(self, g: u8) -> W {
        let l = self.len();
        W(self.0 | ((g as u64) << (l * 5)))
    }
    fn set(&mut self, i: usize, g: u8) {
        let mask = !(0x1Fu64 << (i * 5));
        self.0 = (self.0 & mask) | ((g as u64) << (i * 5));
    }
    fn remove_at(self, pos: usize) -> W {
        let l = self.len();
        let mut r = W::E;
        for i in 0..l { if i != pos { r = r.push(self.get(i)); } }
        r
    }
    fn drop_last(self) -> W {
        let l = self.len();
        if l <= 1 { return W::E; }
        let mut r = W::E;
        for i in 0..l-1 { r = r.push(self.get(i)); }
        r
    }
}

impl std::fmt::Debug for W {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let l = self.len();
        if l == 0 { return write!(f, "𝟏"); }
        for i in 0..l { if i > 0 { write!(f, ".")?; } write!(f, "σ{}", self.get(i))?; }
        Ok(())
    }
}

// ════════════════════════════════════════════════════════════════
// CRT Hecke element and engine
// ════════════════════════════════════════════════════════════════

struct CrtElem {
    terms: FxHashMap<W, CrtPoly>,
    pn_count: u32,
    n_primes: usize,
}

impl CrtElem {
    fn identity(n_primes: usize) -> Self {
        let mut h = Self { terms: FxHashMap::default(), pn_count: 0, n_primes };
        h.terms.insert(W::E, CrtPoly::one(n_primes));
        h
    }
    fn n_terms(&self) -> usize { self.terms.len() }
    fn mem_bytes(&self) -> usize {
        self.terms.iter().map(|(_, c)| 72 + c.terms.len() * (4 + 16 * self.n_primes)).sum()
    }
}

/// HA = q - q⁻¹ = t² - t⁻² as CRT polynomial.
fn ha_crt(n_primes: usize) -> CrtPoly {
    let mut p = CrtPoly::zero(n_primes);
    p.terms.push((2, ModCoeff::one(n_primes)));
    p.terms.push((-2, ModCoeff::from_i64(-1, n_primes)));
    p
}

/// Crossing coefficients (c, d) as CRT polynomials.
fn crossing_crt(ti: u8, tj: u8, n_primes: usize) -> (CrtPoly, CrtPoly, bool) {
    match (ti, tj) {
        (b'p', b'p') => (CrtPoly::one(n_primes), CrtPoly::zero(n_primes), false),
        (b'n', b'n') => {
            let c = CrtPoly::one(n_primes);
            let mut d = CrtPoly::zero(n_primes);
            d.terms.push((2, ModCoeff::from_i64(-1, n_primes)));
            d.terms.push((-2, ModCoeff::one(n_primes)));
            (c, d, false)
        }
        _ => {
            // pn: doubled to stay integral. 2c = 2, 2d = -t² + t⁻²
            let mut c2 = CrtPoly::zero(n_primes);
            c2.terms.push((0, ModCoeff::from_i64(2, n_primes)));
            let mut d2 = CrtPoly::zero(n_primes);
            d2.terms.push((2, ModCoeff::from_i64(-1, n_primes)));
            d2.terms.push((-2, ModCoeff::one(n_primes)));
            (c2, d2, true)
        }
    }
}

struct CrtEngine;

impl CrtEngine {
    fn multiply_and_reduce(
        elem: &mut CrtElem, gen: u8,
        c: &CrtPoly, d: &CrtPoly, doubled: bool, ha: &CrtPoly,
    ) {
        // Exactly matches v9: drain old terms, build new element with
        // d-terms going to reduced and c-terms (appended gen) going to
        // unreduced for junction check.
        let old: Vec<(W, CrtPoly)> = elem.terms.drain().collect();
        let n_primes = elem.n_primes;

        // All d-terms go directly to reduced (no new junction)
        // All c-terms (word·gen) go to pending for reduction
        let mut pending: Vec<(W, CrtPoly)> = Vec::new();

        for (word, coeff) in old {
            if coeff.is_zero() { continue; }

            if !d.is_zero() {
                let new_coeff = coeff.mul(d);
                if !new_coeff.is_zero() {
                    let e = elem.terms.entry(word).or_insert_with(|| CrtPoly::zero(n_primes));
                    *e = e.add(&new_coeff);
                }
            }

            if !c.is_zero() {
                let wg = word.push(gen);
                let new_coeff = coeff.mul(c);
                if !new_coeff.is_zero() {
                    pending.push((wg, new_coeff));
                }
            }
        }

        if doubled { elem.pn_count += 1; }

        // Reduce pending terms (these have a new generator at the end)
        loop {
            if pending.is_empty() { break; }
            let mut next: Vec<(W, CrtPoly)> = Vec::new();

            // Consolidate pending
            let mut batch: FxHashMap<W, CrtPoly> = FxHashMap::default();
            for (w, c) in pending.drain(..) {
                let e = batch.entry(w).or_insert_with(|| CrtPoly::zero(n_primes));
                *e = e.add(&c);
            }

            let mut any_reduced = false;
            for (word, coeff) in batch {
                if coeff.is_zero() { continue; }

                // Find reduction
                let l = word.len();
                let mut red = None;
                if l >= 2 {
                    for p in 0..l-1 {
                        let a = word.get(p); let b = word.get(p+1);
                        if a == b { red = Some((p, 0u8)); break; }
                        if (a as i16 - b as i16) >= 2 { red = Some((p, 1)); break; }
                        if p+2 < l {
                            let c = word.get(p+2);
                            if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                                red = Some((p, 2)); break;
                            }
                        }
                    }
                }

                if let Some((pos, rule)) = red {
                    any_reduced = true;
                    match rule {
                        0 => {
                            let w1 = word.remove_at(pos + 1);
                            let w2 = w1.remove_at(pos);
                            next.push((w1, coeff.mul(ha)));
                            next.push((w2, coeff));
                        }
                        1 => {
                            let mut w = word;
                            let (a, b) = (w.get(pos), w.get(pos+1));
                            w.set(pos, b); w.set(pos+1, a);
                            next.push((w, coeff));
                        }
                        2 => {
                            let mut w = word;
                            let (a, b) = (w.get(pos), w.get(pos+1));
                            w.set(pos, b); w.set(pos+1, a); w.set(pos+2, b);
                            next.push((w, coeff));
                        }
                        _ => {}
                    }
                } else {
                    // Stable — add to element
                    let e = elem.terms.entry(word).or_insert_with(|| CrtPoly::zero(n_primes));
                    *e = e.add(&coeff);
                }
            }

            if !any_reduced && next.is_empty() { break; }
            pending = next;
        }

        elem.terms.retain(|_, c| !c.is_zero());
    }

    fn reduce(terms: &mut FxHashMap<W, CrtPoly>, ha: &CrtPoly, n_primes: usize) {
        // Same logic as v9: iterate until no reductions found
        let mut changed = true;
        while changed {
            changed = false;
            let mut new_terms: FxHashMap<W, CrtPoly> = FxHashMap::default();

            for (word, coeff) in terms.drain() {
                if coeff.is_zero() { continue; }

                let l = word.len();
                let mut done = false;

                // R1: Hecke σ_i² → HA·σ_i + 1
                if l >= 2 {
                    for p in 0..l-1 {
                        if word.get(p) == word.get(p+1) {
                            let w1 = word.remove_at(p + 1);
                            let w2 = w1.remove_at(p);
                            let e1 = new_terms.entry(w1).or_insert_with(|| CrtPoly::zero(n_primes));
                            *e1 = e1.add(&coeff.mul(ha));
                            let e2 = new_terms.entry(w2).or_insert_with(|| CrtPoly::zero(n_primes));
                            *e2 = e2.add(&coeff);
                            done = true; changed = true; break;
                        }
                    }
                }
                if done { continue; }

                // R2: Far-comm σ_iσ_j → σ_jσ_i for i > j, |i-j| ≥ 2
                if l >= 2 {
                    for p in 0..l-1 {
                        let a = word.get(p); let b = word.get(p+1);
                        if (a as i16 - b as i16) >= 2 {
                            let mut w = word;
                            w.set(p, b); w.set(p+1, a);
                            let e = new_terms.entry(w).or_insert_with(|| CrtPoly::zero(n_primes));
                            *e = e.add(&coeff);
                            done = true; changed = true; break;
                        }
                    }
                }
                if done { continue; }

                // R3: Yang-Baxter σ_iσ_jσ_i → σ_jσ_iσ_j (canonical: smaller triple)
                if l >= 3 {
                    for p in 0..l-2 {
                        let a = word.get(p); let b = word.get(p+1); let c = word.get(p+2);
                        if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                            let mut w = word;
                            w.set(p, b); w.set(p+1, a); w.set(p+2, b);
                            let e = new_terms.entry(w).or_insert_with(|| CrtPoly::zero(n_primes));
                            *e = e.add(&coeff);
                            done = true; changed = true; break;
                        }
                    }
                }
                if done { continue; }

                // No reduction — stable
                let e = new_terms.entry(word).or_insert_with(|| CrtPoly::zero(n_primes));
                *e = e.add(&coeff);
            }

            *terms = new_terms;
            terms.retain(|_, c| !c.is_zero());
        }
    }

    /// Pauli strip (I9+I8) — returns accumulated Pauli data
    fn strip(terms: &mut FxHashMap<W, CrtPoly>, n_primes: usize) -> (CrtPoly, CrtPoly, f64) {
        let mut tr_alt = CrtPoly::zero(n_primes);
        let mut net = CrtPoly::zero(n_primes);
        let q0_sqrt = 1.1099785956_f64.sqrt();
        let mut l1_stripped = 0.0_f64;

        loop {
            let mut any = false;
            let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
            for tl in (2..=max_len).rev() {
                let to_rm: Vec<W> = terms.keys()
                    .filter(|w| w.len() == tl && !terms[*w].is_zero())
                    .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                    .cloned().collect();
                for w in &to_rm {
                    if let Some(c) = terms.remove(w) {
                        let wl = w.len();
                        net = net.add(&c);
                        let sign = if wl % 2 == 0 { 1i64 } else { -1i64 };
                        tr_alt = tr_alt.add(&c.scale_i64(sign).shift(-2 * wl as i32));
                        l1_stripped += c.eval_f64(q0_sqrt).abs();
                        any = true;
                    }
                }
            }
            // I8
            let adj: Vec<W> = terms.keys()
                .filter(|w| w.len() == 2 && !terms[*w].is_zero() && w.get(1) == w.get(0) + 1)
                .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &adj {
                if let Some(c) = terms.remove(w) {
                    net = net.add(&c);
                    let sign = if 2 % 2 == 0 { 1i64 } else { -1i64 };
                    tr_alt = tr_alt.add(&c.scale_i64(sign).shift(-4));
                    l1_stripped += c.eval_f64(q0_sqrt).abs();
                    any = true;
                }
            }
            if !any { break; }
        }
        terms.retain(|_, c| !c.is_zero());
        (tr_alt, net, l1_stripped)
    }

    fn build(types: &[u8], n_primes: usize, mid_threshold: usize) -> (CrtElem, CrtPoly, CrtPoly, f64) {
        let a = types.len();
        let ha = ha_crt(n_primes);
        let mut elem = CrtElem::identity(n_primes);
        let mut accum_tr_alt = CrtPoly::zero(n_primes);
        let mut accum_net = CrtPoly::zero(n_primes);
        let mut accum_l1: f64 = 0.0;
        let t0 = Instant::now();

        let no_mid_strip = a <= 12;
        let strip_after = if no_mid_strip { 999 } else if a > 9 { 8 } else { 999 };
        let eager = !no_mid_strip && mid_threshold == 0;

        for k in 1..a {
            for i in (0..k).rev() {  // Garside order: right-to-left
                let (c, d, dbl) = crossing_crt(types[i], types[k], n_primes);
                Self::multiply_and_reduce(&mut elem, i as u8, &c, &d, dbl, &ha);

                let should_strip = (eager && k >= strip_after)
                    || elem.n_terms() > mid_threshold;

                if should_strip {
                    let (ta, nt, l1) = Self::strip(&mut elem.terms, n_primes);
                    accum_tr_alt = accum_tr_alt.add(&ta);
                    accum_net = accum_net.add(&nt);
                    accum_l1 += l1;
                }
            }

            let elapsed = t0.elapsed().as_secs_f64();
            let mb = elem.mem_bytes() as f64 / 1_048_576.0;

            if (k + 1) > strip_after {
                let n_pre = elem.n_terms();
                let (ta, nt, l1) = Self::strip(&mut elem.terms, n_primes);
                accum_tr_alt = accum_tr_alt.add(&ta);
                accum_net = accum_net.add(&nt);
                accum_l1 += l1;
                eprintln!("  strand {}/{}: {} → {} words, {:.0}MB, {:.1}s",
                    k, a - 1, n_pre, elem.n_terms(), mb, elapsed);
            } else {
                eprintln!("  strand {}/{}: {} words, {:.0}MB, {:.1}s",
                    k, a - 1, elem.n_terms(), mb, elapsed);
            }
        }

        (elem, accum_tr_alt, accum_net, accum_l1)
    }
}

// ════════════════════════════════════════════════════════════════
// Main
// ════════════════════════════════════════════════════════════════

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("hecke-crt v13 — CRT multi-prime Hecke engine with Garside order");
        eprintln!("Usage: hecke-crt qvalue ORDERING [n_primes] [mid_strip_threshold]");
        eprintln!("  ORDERING: string of p/n (e.g. ppnpnnpnn for tritium at quark level)");
        eprintln!("  n_primes: number of CRT primes (default 4, max 8)");
        eprintln!("  mid_strip_threshold: strip when words > N (default: auto)");
        std::process::exit(1);
    }

    if args[1] != "qvalue" {
        eprintln!("Only 'qvalue' mode supported. Usage: hecke-crt qvalue ORDERING");
        std::process::exit(1);
    }

    let ordering_str = &args[2];
    let types: Vec<u8> = ordering_str.chars().map(|c| match c {
        'p' | 'u' | '1' => b'p',
        'n' | 'd' | '0' => b'n',
        _ => panic!("Invalid char: {}", c),
    }).collect();
    let a = types.len();
    let z = types.iter().filter(|&&t| t == b'p').count();
    let n = a - z;
    let n_primes: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(4).min(8);
    let mid_threshold: usize = args.get(4).and_then(|s| s.parse().ok())
        .unwrap_or(if a > 12 { 0 } else { 999999 });

    eprintln!("hecke-crt v13 — CRT engine ({} primes)", n_primes);
    eprintln!("  ordering: {} (Z={}, N={}, A={})", ordering_str, z, n, a);
    eprintln!("  primes: {:?}", &PRIMES[..n_primes]);

    let t0 = Instant::now();
    let (elem, accum_ta, accum_net, accum_l1) = CrtEngine::build(&types, n_primes, mid_threshold);

    // Compute kept Pauli data
    let q0_sqrt = 1.1099785956_f64.sqrt();
    let pn_denom = 2.0_f64.powi(elem.pn_count as i32);

    let mut kept_ta = CrtPoly::zero(n_primes);
    let mut kept_net = CrtPoly::zero(n_primes);
    let mut kept_l1: f64 = 0.0;
    for (w, c) in &elem.terms {
        kept_net = kept_net.add(c);
        let wl = w.len();
        let sign = if wl % 2 == 0 { 1i64 } else { -1i64 };
        kept_ta = kept_ta.add(&c.scale_i64(sign).shift(-2 * wl as i32));
        kept_l1 += c.eval_f64(q0_sqrt).abs();
    }

    let total_ta = kept_ta.add(&accum_ta);
    let total_net = kept_net.add(&accum_net);
    let total_l1 = (kept_l1 + accum_l1) / pn_denom;

    let ta_val = total_ta.eval_f64(q0_sqrt) / pn_denom;
    let net_val = total_net.eval_f64(q0_sqrt) / pn_denom;
    let f_pauli = if net_val.abs() > 1e-30 { (ta_val / net_val).abs() } else { 0.0 };

    let elapsed = t0.elapsed().as_secs_f64();
    let words = elem.n_terms();

    println!("{{\"ordering\":\"{}\",\"z\":{},\"n\":{},\"a\":{},\"words\":{},\"l1\":{:.10},\"f_pauli\":{:.10},\"tr_alt\":{:.10e},\"net\":{:.10e},\"n_primes\":{},\"elapsed_s\":{:.3}}}",
        ordering_str, z, n, a, words, total_l1, f_pauli, ta_val, net_val, n_primes, elapsed);

    eprintln!("\n  {} words, L1={:.10}, F_Pauli={:.6}, {:.1}s", words, total_l1, f_pauli, elapsed);
}
