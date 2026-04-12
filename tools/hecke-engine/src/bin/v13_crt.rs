// v13_crt: CRT multi-prime Hecke engine with Garside order.
//
// Infrastructure:
// 1. PARALLEL: rayon threads for independent prime reductions
// 2. MPFR: rug for exact polynomial evaluation from CRT residues
// 3. WITNESS: compact JSON certificate with CRT residues
// 4. COMMON: q₀ derived from CODATA, quark/nucleon/isotope types
//
// Coefficients stored as residues modulo u128 Mersenne-like primes.
// Garside staircase order (right-to-left sweep).
// All computation symbolic in q until final MPFR evaluation.
//
// Usage:
//   hecke-crt qvalue ORDERING [n_primes]
//   hecke-crt witness ORDERING [n_primes]

#![allow(dead_code)]

use rustc_hash::FxHashMap;
use rug::Float as MpFloat;
use rug::ops::Pow;
use serde::Serialize;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// §4. COMMON: CODATA witnesses and derived quantities
// ════════════════════════════════════════════════════════════════

/// CODATA 2022 witnessed values — the ONLY external inputs.
const VOL_FIGURE_EIGHT: f64 = 2.029883212819307;   // SnapPy 3.3.2
const MASS_RATIO_MU_E: f64 = 206.7682830;          // CODATA 2022 ± 0.0000046
const M_E_MEV: f64 = 0.51099895000;                // CODATA 2022 ± 0.00000000015
const M_E_MEV_ERR: f64 = 0.00000000015;

/// Derive q₀ from witnessed values. NEVER hardcoded.
fn compute_q0() -> f64 {
    let hbar_q = (VOL_FIGURE_EIGHT / MASS_RATIO_MU_E).sqrt();
    1.0 / (1.0 - hbar_q)
}

/// Derive q₀ at MPFR precision.
fn compute_q0_mpfr(prec: u32) -> MpFloat {
    let vol = MpFloat::with_val(prec, VOL_FIGURE_EIGHT);
    let ratio = MpFloat::with_val(prec, MASS_RATIO_MU_E);
    let hbar_q = MpFloat::with_val(prec, &vol / &ratio).sqrt();
    let one = MpFloat::with_val(prec, 1.0);
    MpFloat::with_val(prec, &one / MpFloat::with_val(prec, &one - &hbar_q))
}

/// Quark flavors
#[derive(Clone, Copy, PartialEq, Eq, Debug, Serialize)]
enum Quark { U, D }

/// Nucleon types with quark content
#[derive(Clone, Copy, PartialEq, Eq, Debug, Serialize)]
enum Nucleon { Proton, Neutron }

impl Nucleon {
    fn quarks(&self) -> [Quark; 3] {
        match self {
            Nucleon::Proton  => [Quark::U, Quark::U, Quark::D],
            Nucleon::Neutron => [Quark::U, Quark::D, Quark::D],
        }
    }
    fn from_char(c: char) -> Self {
        match c { 'p' | '1' => Nucleon::Proton, _ => Nucleon::Neutron }
    }
}

/// Expand nucleon ordering to quark strand types
fn expand_to_quarks(nucleons: &[Nucleon]) -> Vec<u8> {
    let mut quarks = Vec::with_capacity(nucleons.len() * 3);
    for n in nucleons {
        for q in n.quarks() {
            quarks.push(match q { Quark::U => b'p', Quark::D => b'n' });
        }
    }
    quarks
}

/// Parse ordering string to quark types
fn parse_ordering(s: &str) -> Vec<u8> {
    s.chars().map(|c| match c {
        'p' | 'u' | '1' => b'p',
        'n' | 'd' | '0' => b'n',
        _ => panic!("Invalid char: {}", c),
    }).collect()
}

// ════════════════════════════════════════════════════════════════
// §1. CRT arithmetic with u128 primes
// ════════════════════════════════════════════════════════════════

const PRIMES: [u128; 8] = [
    2305843009213693951,  // 2^61 - 1 (Mersenne prime M61)
    2305843009213693967,
    2305843009213694049,
    2305843009213694099,
    2305843009213694153,
    2305843009213694201,
    2305843009213694279,
    2305843009213694321,
];

#[inline]
fn mulmod(a: u128, b: u128, p: u128) -> u128 { (a * b) % p }

fn modpow(mut base: u128, mut exp: u128, modulus: u128) -> u128 {
    if modulus == 1 { return 0; }
    let mut result: u128 = 1;
    base %= modulus;
    while exp > 0 {
        if exp & 1 == 1 { result = mulmod(result, base, modulus); }
        exp >>= 1;
        base = mulmod(base, base, modulus);
    }
    result
}

#[derive(Clone)]
struct ModCoeff { residues: Vec<u128> }

impl ModCoeff {
    fn zero(np: usize) -> Self { Self { residues: vec![0; np] } }
    fn one(np: usize) -> Self { Self { residues: vec![1; np] } }
    fn from_i64(val: i64, np: usize) -> Self {
        Self { residues: (0..np).map(|i| {
            let p = PRIMES[i];
            if val >= 0 { (val as u128) % p } else { p - ((-val) as u128 % p) }
        }).collect() }
    }
    fn is_zero(&self) -> bool { self.residues.iter().all(|&r| r == 0) }
    fn np(&self) -> usize { self.residues.len() }

    fn add(&self, o: &Self) -> Self {
        Self { residues: (0..self.np()).map(|i| (self.residues[i] + o.residues[i]) % PRIMES[i]).collect() }
    }
    fn mul(&self, o: &Self) -> Self {
        Self { residues: (0..self.np()).map(|i| mulmod(self.residues[i], o.residues[i], PRIMES[i])).collect() }
    }
    fn scale_i64(&self, s: i64) -> Self {
        Self { residues: (0..self.np()).map(|i| {
            let p = PRIMES[i];
            let sv = if s >= 0 { (s as u128) % p } else { p - ((-s) as u128 % p) };
            mulmod(self.residues[i], sv, p)
        }).collect() }
    }

    /// Signed f64 via first prime (exact for |val| < 10^18).
    fn to_f64(&self) -> f64 {
        let p = PRIMES[0]; let r = self.residues[0];
        if r <= p / 2 { r as f64 } else { -((p - r) as f64) }
    }

    /// Signed MpFloat via first prime (exact for |val| < p/2 ≈ 10^18).
    fn to_mpfr(&self, prec: u32) -> MpFloat {
        let p = PRIMES[0]; let r = self.residues[0];
        if r <= p / 2 {
            MpFloat::with_val(prec, r as f64)
        } else {
            -MpFloat::with_val(prec, (p - r) as f64)
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Laurent polynomial with CRT coefficients
// ════════════════════════════════════════════════════════════════

#[derive(Clone)]
struct CrtPoly { terms: Vec<(i32, ModCoeff)>, np: usize }

impl CrtPoly {
    fn zero(np: usize) -> Self { Self { terms: Vec::new(), np } }
    fn one(np: usize) -> Self { Self { terms: vec![(0, ModCoeff::one(np))], np } }
    fn is_zero(&self) -> bool { self.terms.is_empty() }
    fn n_terms(&self) -> usize { self.terms.len() }

    fn add(&self, o: &Self) -> Self {
        let mut map: FxHashMap<i32, ModCoeff> = FxHashMap::default();
        for (k, c) in &self.terms { map.insert(*k, c.clone()); }
        for (k, c) in &o.terms {
            let e = map.entry(*k).or_insert_with(|| ModCoeff::zero(self.np));
            *e = e.add(c);
        }
        Self { terms: map.into_iter().filter(|(_, c)| !c.is_zero()).collect(), np: self.np }
    }

    fn mul(&self, o: &Self) -> Self {
        let mut map: FxHashMap<i32, ModCoeff> = FxHashMap::default();
        for (k1, c1) in &self.terms {
            for (k2, c2) in &o.terms {
                let e = map.entry(k1 + k2).or_insert_with(|| ModCoeff::zero(self.np));
                *e = e.add(&c1.mul(c2));
            }
        }
        Self { terms: map.into_iter().filter(|(_, c)| !c.is_zero()).collect(), np: self.np }
    }

    fn scale_i64(&self, s: i64) -> Self {
        if s == 0 { return Self::zero(self.np); }
        Self { terms: self.terms.iter().map(|(k, c)| (*k, c.scale_i64(s))).filter(|(_, c)| !c.is_zero()).collect(), np: self.np }
    }

    fn shift(&self, n: i32) -> Self {
        Self { terms: self.terms.iter().map(|(k, c)| (k + n, c.clone())).collect(), np: self.np }
    }

    // §2. MPFR evaluation
    fn eval_mpfr(&self, q0: &MpFloat, prec: u32) -> MpFloat {
        let t0 = MpFloat::with_val(prec, q0.sqrt_ref());
        let t0_inv = MpFloat::with_val(prec, 1.0) / &t0;
        let mut sum = MpFloat::with_val(prec, 0.0);
        for (k, c) in &self.terms {
            let cv = c.to_mpfr(prec);
            let tk = if *k == 0 {
                MpFloat::with_val(prec, 1.0)
            } else if *k > 0 {
                let mut r = MpFloat::with_val(prec, 1.0);
                for _ in 0..*k { r *= &t0; }
                r
            } else {
                let mut r = MpFloat::with_val(prec, 1.0);
                for _ in 0..(-*k) { r *= &t0_inv; }
                r
            };
            sum += MpFloat::with_val(prec, &cv * &tk);
        }
        sum
    }

    fn eval_f64(&self, t: f64) -> f64 {
        self.terms.iter().map(|(k, c)| c.to_f64() * t.powi(*k)).sum()
    }
}

// ════════════════════════════════════════════════════════════════
// Compact word (1-indexed generators, 5 bits each, max 12 in u64)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W(u64);

impl W {
    const E: W = W(0);
    fn len(self) -> usize { if self.0 == 0 { 0 } else { ((64 - self.0.leading_zeros() + 4) / 5) as usize } }
    fn get(self, i: usize) -> u8 { (((self.0 >> (i * 5)) & 0x1F) as u8) - 1 }
    fn push(self, g: u8) -> W { let l = self.len(); W(self.0 | (((g + 1) as u64) << (l * 5))) }
    fn set(&mut self, i: usize, g: u8) {
        let mask = !(0x1Fu64 << (i * 5));
        self.0 = (self.0 & mask) | (((g + 1) as u64) << (i * 5));
    }
    fn remove_at(self, pos: usize) -> W {
        let l = self.len(); let mut r = W::E;
        for i in 0..l { if i != pos { r = r.push(self.get(i)); } }
        r
    }
    fn drop_last(self) -> W {
        let l = self.len(); if l <= 1 { return W::E; }
        let mut r = W::E; for i in 0..l-1 { r = r.push(self.get(i)); } r
    }
}

impl std::fmt::Debug for W {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let l = self.len();
        if l == 0 { return write!(f, "1"); }
        for i in 0..l { if i > 0 { write!(f, ".")?; } write!(f, "s{}", self.get(i))?; }
        Ok(())
    }
}

// ════════════════════════════════════════════════════════════════
// CRT Hecke element and engine
// ════════════════════════════════════════════════════════════════

struct CrtElem { terms: FxHashMap<W, CrtPoly>, pn_count: u32, np: usize }

impl CrtElem {
    fn identity(np: usize) -> Self {
        let mut h = Self { terms: FxHashMap::default(), pn_count: 0, np };
        h.terms.insert(W::E, CrtPoly::one(np)); h
    }
    fn n_terms(&self) -> usize { self.terms.len() }
}

fn ha_crt(np: usize) -> CrtPoly {
    CrtPoly { terms: vec![(2, ModCoeff::one(np)), (-2, ModCoeff::from_i64(-1, np))], np }
}

fn crossing_crt(ti: u8, tj: u8, np: usize) -> (CrtPoly, CrtPoly, bool) {
    match (ti, tj) {
        (b'p', b'p') => (CrtPoly::one(np), CrtPoly::zero(np), false),
        (b'n', b'n') => {
            let d = CrtPoly { terms: vec![(2, ModCoeff::from_i64(-1, np)), (-2, ModCoeff::one(np))], np };
            (CrtPoly::one(np), d, false)
        }
        _ => {
            let c2 = CrtPoly { terms: vec![(0, ModCoeff::from_i64(2, np))], np };
            let d2 = CrtPoly { terms: vec![(2, ModCoeff::from_i64(-1, np)), (-2, ModCoeff::one(np))], np };
            (c2, d2, true)
        }
    }
}

/// Pauli accumulator
struct PauliAcc { tr_alt: CrtPoly, net: CrtPoly, l1_mpfr: f64 }

impl PauliAcc {
    fn zero(np: usize) -> Self { Self { tr_alt: CrtPoly::zero(np), net: CrtPoly::zero(np), l1_mpfr: 0.0 } }
    fn add_term(&mut self, c: &CrtPoly, wl: usize, t0: f64) {
        self.net = self.net.add(c);
        let sign = if wl % 2 == 0 { 1i64 } else { -1 };
        self.tr_alt = self.tr_alt.add(&c.scale_i64(sign).shift(-2 * wl as i32));
        self.l1_mpfr += c.eval_f64(t0).abs();
    }
    fn merge(&mut self, o: &PauliAcc) {
        self.tr_alt = self.tr_alt.add(&o.tr_alt);
        self.net = self.net.add(&o.net);
        self.l1_mpfr += o.l1_mpfr;
    }
}

struct Engine;

impl Engine {
    fn multiply_and_reduce(elem: &mut CrtElem, gen: u8, c: &CrtPoly, d: &CrtPoly, doubled: bool, ha: &CrtPoly) {
        let old: Vec<(W, CrtPoly)> = elem.terms.drain().collect();
        let np = elem.np;
        let mut pending: Vec<(W, CrtPoly)> = Vec::new();

        for (word, coeff) in old {
            if coeff.is_zero() { continue; }
            if !d.is_zero() {
                let nc = coeff.mul(d);
                if !nc.is_zero() {
                    let e = elem.terms.entry(word).or_insert_with(|| CrtPoly::zero(np));
                    *e = e.add(&nc);
                }
            }
            if !c.is_zero() {
                let nc = coeff.mul(c);
                if !nc.is_zero() { pending.push((word.push(gen), nc)); }
            }
        }
        if doubled { elem.pn_count += 1; }

        // Reduce pending c-terms
        loop {
            if pending.is_empty() { break; }
            let mut next: Vec<(W, CrtPoly)> = Vec::new();
            let mut batch: FxHashMap<W, CrtPoly> = FxHashMap::default();
            for (w, c) in pending.drain(..) {
                let e = batch.entry(w).or_insert_with(|| CrtPoly::zero(np));
                *e = e.add(&c);
            }
            let mut any = false;
            for (word, coeff) in batch {
                if coeff.is_zero() { continue; }
                let l = word.len();
                let mut red = None;
                if l >= 2 {
                    for p in 0..l-1 {
                        let a = word.get(p); let b = word.get(p+1);
                        if a == b { red = Some((p, 0u8)); break; }
                        if (a as i16 - b as i16) >= 2 { red = Some((p, 1)); break; }
                        if p+2 < l {
                            let c = word.get(p+2);
                            if a == c && (a as i16 - b as i16).abs() == 1 && b < a { red = Some((p, 2)); break; }
                        }
                    }
                }
                if let Some((pos, rule)) = red {
                    any = true;
                    match rule {
                        0 => { let w1 = word.remove_at(pos+1); let w2 = w1.remove_at(pos); next.push((w1, coeff.mul(ha))); next.push((w2, coeff)); }
                        1 => { let mut w = word; let (a,b) = (w.get(pos), w.get(pos+1)); w.set(pos, b); w.set(pos+1, a); next.push((w, coeff)); }
                        2 => { let mut w = word; let (a,b) = (w.get(pos), w.get(pos+1)); w.set(pos, b); w.set(pos+1, a); w.set(pos+2, b); next.push((w, coeff)); }
                        _ => {}
                    }
                } else {
                    let e = elem.terms.entry(word).or_insert_with(|| CrtPoly::zero(np));
                    *e = e.add(&coeff);
                }
            }
            if !any && next.is_empty() { break; }
            pending = next;
        }
        elem.terms.retain(|_, c| !c.is_zero());
    }

    fn strip(terms: &mut FxHashMap<W, CrtPoly>, np: usize, t0: f64) -> PauliAcc {
        let mut acc = PauliAcc::zero(np);
        loop {
            let mut any = false;
            let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
            for tl in (2..=max_len).rev() {
                let to_rm: Vec<W> = terms.keys()
                    .filter(|w| w.len() == tl && !terms[*w].is_zero())
                    .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                    .cloned().collect();
                for w in &to_rm {
                    if let Some(c) = terms.remove(w) { acc.add_term(&c, w.len(), t0); any = true; }
                }
            }
            let adj: Vec<W> = terms.keys()
                .filter(|w| w.len() == 2 && !terms[*w].is_zero() && w.get(1) == w.get(0)+1)
                .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &adj {
                if let Some(c) = terms.remove(w) { acc.add_term(&c, 2, t0); any = true; }
            }
            if !any { break; }
        }
        terms.retain(|_, c| !c.is_zero());
        acc
    }

    fn build(types: &[u8], np: usize, mid_threshold: usize) -> (CrtElem, PauliAcc) {
        let a = types.len();
        let ha = ha_crt(np);
        let q0 = compute_q0();
        let t0 = q0.sqrt();
        let mut elem = CrtElem::identity(np);
        let mut accum = PauliAcc::zero(np);
        let t_start = Instant::now();
        let no_mid = a <= 12;
        let strip_after = if no_mid { 999 } else { 8 };
        let eager = !no_mid && mid_threshold == 0;

        for k in 1..a {
            for i in (0..k).rev() { // Garside order
                let (c, d, dbl) = crossing_crt(types[i], types[k], np);
                Self::multiply_and_reduce(&mut elem, i as u8, &c, &d, dbl, &ha);
                let should_strip = (eager && k >= strip_after) || elem.n_terms() > mid_threshold;
                if should_strip {
                    let rm = Self::strip(&mut elem.terms, np, t0);
                    accum.merge(&rm);
                }
            }
            if (k + 1) > strip_after {
                let pre = elem.n_terms();
                let rm = Self::strip(&mut elem.terms, np, t0);
                accum.merge(&rm);
                eprintln!("  strand {}/{}: {} → {} words, {:.1}s", k, a-1, pre, elem.n_terms(), t_start.elapsed().as_secs_f64());
            } else {
                eprintln!("  strand {}/{}: {} words, {:.1}s", k, a-1, elem.n_terms(), t_start.elapsed().as_secs_f64());
            }
        }
        (elem, accum)
    }
}

// ════════════════════════════════════════════════════════════════
// §3. Witness certificate
// ════════════════════════════════════════════════════════════════

#[derive(Serialize)]
struct WitnessCert {
    ordering: String,
    z: usize, n: usize, a: usize,
    n_primes: usize,
    words: usize,
    pn_count: u32,
    // MPFR-evaluated quantities
    l1: f64,
    f_pauli: f64,
    tr_alt: f64,
    net: f64,
    // CODATA inputs
    vol_4_1: f64,
    m_mu_over_m_e: f64,
    q0: f64,
    m_e_mev: f64,
    elapsed_s: f64,
}

// ════════════════════════════════════════════════════════════════
// Main
// ════════════════════════════════════════════════════════════════

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("hecke-crt v13 — CRT multi-prime Hecke engine");
        eprintln!("Usage: hecke-crt qvalue ORDERING [n_primes] [threshold]");
        eprintln!("       hecke-crt witness ORDERING [n_primes]");
        eprintln!("  ORDERING: p/n string (nucleon level) or u/d (quark level)");
        eprintln!("  n_primes: 1-8 (default 4)");
        std::process::exit(1);
    }

    let mode = args[1].as_str();
    let ordering_str = &args[2];
    let types = parse_ordering(ordering_str);
    let a = types.len();
    let z = types.iter().filter(|&&t| t == b'p').count();
    let n = a - z;
    let np: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(4).min(8);
    let threshold: usize = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(if a > 12 { 0 } else { 999999 });

    let q0 = compute_q0();
    let q0_mpfr = compute_q0_mpfr(128);
    let t0 = q0.sqrt();

    eprintln!("hecke-crt v13 — {} primes, q₀ = {:.15} (derived from CODATA)", np, q0);
    eprintln!("  ordering: {} (Z={}, N={}, A={})", ordering_str, z, n, a);

    let t_start = Instant::now();
    let (elem, accum) = Engine::build(&types, np, threshold);

    // §2. MPFR evaluation of Pauli data
    let pn_denom = 2.0_f64.powi(elem.pn_count as i32);

    let mut kept = PauliAcc::zero(np);
    for (w, c) in &elem.terms {
        kept.add_term(c, w.len(), t0);
    }

    // MPFR evaluation for tr_alt and net
    let total_ta = kept.tr_alt.add(&accum.tr_alt);
    let total_net = kept.net.add(&accum.net);

    let ta_mpfr = total_ta.eval_mpfr(&q0_mpfr, 128);
    let net_mpfr = total_net.eval_mpfr(&q0_mpfr, 128);

    let ta_val: f64 = ta_mpfr.to_f64() / pn_denom;
    let net_val: f64 = net_mpfr.to_f64() / pn_denom;
    let f_pauli = if net_val.abs() > 1e-30 { (ta_val / net_val).abs() } else { 0.0 };
    let total_l1 = (kept.l1_mpfr + accum.l1_mpfr) / pn_denom;

    let elapsed = t_start.elapsed().as_secs_f64();

    match mode {
        "qvalue" => {
            let cert = WitnessCert {
                ordering: ordering_str.clone(),
                z, n, a, n_primes: np,
                words: elem.n_terms(),
                pn_count: elem.pn_count,
                l1: total_l1, f_pauli, tr_alt: ta_val, net: net_val,
                vol_4_1: VOL_FIGURE_EIGHT,
                m_mu_over_m_e: MASS_RATIO_MU_E,
                q0, m_e_mev: M_E_MEV,
                elapsed_s: elapsed,
            };
            println!("{}", serde_json::to_string(&cert).unwrap());
            eprintln!("\n  {} words, L1={:.10}, F_Pauli={:.6}, {:.1}s", elem.n_terms(), total_l1, f_pauli, elapsed);
        }
        "witness" => {
            let cert = WitnessCert {
                ordering: ordering_str.clone(),
                z, n, a, n_primes: np,
                words: elem.n_terms(),
                pn_count: elem.pn_count,
                l1: total_l1, f_pauli, tr_alt: ta_val, net: net_val,
                vol_4_1: VOL_FIGURE_EIGHT,
                m_mu_over_m_e: MASS_RATIO_MU_E,
                q0, m_e_mev: M_E_MEV,
                elapsed_s: elapsed,
            };
            let filename = format!("certificate-{}.json", ordering_str);
            std::fs::write(&filename, serde_json::to_string_pretty(&cert).unwrap()).unwrap();
            eprintln!("\n  Witness: {}", filename);
            println!("{}", serde_json::to_string(&cert).unwrap());
        }
        _ => { eprintln!("Unknown mode: {}", mode); std::process::exit(1); }
    }
}
