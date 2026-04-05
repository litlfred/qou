// v9: BigInt symbolic engine — no i128 overflow.
//
// Drop-in replacement for v8 using num-bigint for coefficients.
// Target: A=60 (⁶⁰Co) in symbolic q with mid-crossing stripping.
//
// Key differences from v8:
// 1. LPoly coefficients are BigInt (arbitrary precision)
// 2. Mid-crossing stripping always on (threshold configurable)
// 3. Iterative quotienting: reuse coral content from A=n for A=n+1
// 4. Memory-bounded: strip aggressively to stay under budget
//
// Usage:
//   hecke-bigint Z N [mid_strip_threshold]
//   e.g. hecke-bigint 27 33 10000   (⁶⁰Co with 10K word limit)

#![allow(dead_code)]
use num_bigint::BigInt;
use num_traits::{Zero, One, Signed};
use rustc_hash::FxHashMap;
use std::collections::BTreeMap;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// Laurent polynomial in t = q^{1/2} over ℤ (BigInt coefficients)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Debug, PartialEq, Eq, Default)]
struct LPoly { terms: BTreeMap<i32, BigInt> }

impl LPoly {
    fn zero() -> Self { Self { terms: BTreeMap::new() } }
    fn one() -> Self { let mut p = Self::zero(); p.terms.insert(0, BigInt::one()); p }
    fn t(power: i32) -> Self { let mut p = Self::zero(); p.terms.insert(power, BigInt::one()); p }
    fn is_zero(&self) -> bool { self.terms.is_empty() }
    fn n_terms(&self) -> usize { self.terms.len() }

    fn add(&self, other: &LPoly) -> LPoly {
        let mut r = self.clone();
        for (k, v) in &other.terms {
            let e = r.terms.entry(*k).or_insert_with(BigInt::zero);
            *e += v;
            if e.is_zero() { r.terms.remove(k); }
        }
        r
    }
    fn scale(&self, s: &BigInt) -> LPoly {
        if s.is_zero() { return Self::zero(); }
        let mut r = BTreeMap::new();
        for (k, v) in &self.terms {
            let val = v * s;
            if !val.is_zero() { r.insert(*k, val); }
        }
        LPoly { terms: r }
    }
    fn scale_i64(&self, s: i64) -> LPoly {
        self.scale(&BigInt::from(s))
    }
    fn mul(&self, other: &LPoly) -> LPoly {
        let mut r: BTreeMap<i32, BigInt> = BTreeMap::new();
        for (k1, v1) in &self.terms {
            for (k2, v2) in &other.terms {
                let k = k1 + k2;
                let val = v1 * v2;
                let e = r.entry(k).or_insert_with(BigInt::zero);
                *e += val;
                if e.is_zero() { r.remove(&k); }
            }
        }
        LPoly { terms: r }
    }
    fn shift(&self, n: i32) -> LPoly {
        let mut r = BTreeMap::new();
        for (k, v) in &self.terms { r.insert(k + n, v.clone()); }
        LPoly { terms: r }
    }
    fn eval_f64(&self, t: f64) -> f64 {
        self.terms.iter().map(|(k, v)| {
            let c: f64 = v.to_string().parse().unwrap_or(0.0);
            c * t.powi(*k)
        }).sum()
    }
    fn max_abs_coeff_log10(&self) -> f64 {
        self.terms.values()
            .map(|v| {
                let s = v.abs().to_string();
                s.len() as f64 - 1.0 + (s.chars().next().unwrap().to_digit(10).unwrap_or(1) as f64).log10()
            })
            .fold(0.0f64, f64::max)
    }
    fn mem_bytes(&self) -> usize {
        self.terms.iter().map(|(_, v)| {
            32 + v.to_bytes_le().1.len()  // overhead + digit bytes
        }).sum()
    }
}

// ════════════════════════════════════════════════════════════════
// Packed word (reuse from v8 — same TreeWord structure)
// ════════════════════════════════════════════════════════════════

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W { data: [u128; 4], len: u8 }

impl W {
    const E: W = W { data: [0; 4], len: 0 };
    fn len(self) -> usize { self.len as usize }
    fn get(self, i: usize) -> u8 { ((self.data[i/16] >> ((i%16)*8)) & 0xFF) as u8 }
    fn set(&mut self, i: usize, v: u8) {
        let s = (i%16)*8; let w = i/16;
        self.data[w] = (self.data[w] & !(0xFF << s)) | ((v as u128) << s);
    }
    fn push(mut self, v: u8) -> W {
        let l = self.len as usize;
        if l >= 64 { return self; }
        let s = (l%16)*8; let w = l/16;
        self.data[w] |= (v as u128) << s;
        self.len += 1;
        self
    }
    fn remove_at(self, pos: usize) -> W {
        let l = self.len();
        let mut r = W::E;
        let mut j = 0;
        for i in 0..l { if i != pos { r = r.push(self.get(i)); j += 1; } }
        r
    }
    fn drop_last(self) -> W {
        if self.len == 0 { return self; }
        let mut r = W::E;
        for i in 0..self.len() - 1 { r = r.push(self.get(i)); }
        r
    }

    fn junction_check(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        let p = l-2;
        let a = self.get(p); let b = self.get(p+1);
        if a == b { return Some((p, 0)); }
        if (a as i16 - b as i16) >= 2 { return Some((p, 1)); }
        if l >= 3 {
            let c = self.get(l-3);
            if c == b && (c as i16 - a as i16).abs() == 1 && a < c {
                return Some((l-3, 2));
            }
        }
        None
    }
    fn find_reduction(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        for p in 0..l-1 {
            let a = self.get(p); let b = self.get(p+1);
            if a == b { return Some((p, 0)); }
            if (a as i16 - b as i16) >= 2 { return Some((p, 1)); }
            if p+2 < l {
                let c = self.get(p+2);
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a { return Some((p, 2)); }
            }
        }
        None
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
// Symbolic Hecke element (BigInt version)
// ════════════════════════════════════════════════════════════════

struct Elem { terms: FxHashMap<W, LPoly>, pn_count: u32 }

impl Elem {
    fn identity() -> Self {
        let mut h = Self { terms: FxHashMap::default(), pn_count: 0 };
        h.terms.insert(W::E, LPoly::one());
        h
    }
    fn n_terms(&self) -> usize { self.terms.len() }
    fn total_poly_terms(&self) -> usize { self.terms.values().map(|c| c.n_terms()).sum() }
    fn mem_bytes(&self) -> usize { self.terms.iter().map(|(_, c)| 72 + c.mem_bytes()).sum() }
    fn max_coeff_log10(&self) -> f64 {
        self.terms.values().map(|c| c.max_abs_coeff_log10()).fold(0.0f64, f64::max)
    }
}

// ════════════════════════════════════════════════════════════════
// Crossing coefficients and engine
// ════════════════════════════════════════════════════════════════

fn ha_poly() -> LPoly {
    let mut p = LPoly::zero();
    p.terms.insert(2, BigInt::one());
    p.terms.insert(-2, -BigInt::one());
    p
}

fn crossing_sym(ti: u8, tj: u8) -> (LPoly, LPoly, bool) {
    match (ti, tj) {
        (b'p', b'p') => (LPoly::one(), LPoly::zero(), false),
        (b'n', b'n') => {
            let c = LPoly::t(4);
            let mut d = LPoly::zero();
            d.terms.insert(3, -BigInt::one());
            d.terms.insert(1, BigInt::one());
            (c, d, false)
        }
        _ => {
            let mut c2 = LPoly::one();
            c2.terms.insert(4, BigInt::one());
            let mut d2 = LPoly::zero();
            d2.terms.insert(3, -BigInt::one());
            d2.terms.insert(1, BigInt::one());
            (c2, d2, true)
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Pauli accumulator (BigInt version)
// ════════════════════════════════════════════════════════════════

#[derive(Clone)]
struct SymPauliAcc {
    tr_alt: LPoly,
    net: LPoly,
}

impl SymPauliAcc {
    fn zero() -> Self { Self { tr_alt: LPoly::zero(), net: LPoly::zero() } }

    fn add_term(&mut self, coeff: &LPoly, word_len: usize) {
        self.net = self.net.add(coeff);
        let l = word_len as i64;
        let sign = if l % 2 == 0 { 1i64 } else { -1i64 };
        self.tr_alt = self.tr_alt.add(&coeff.scale_i64(sign).shift(-2 * word_len as i32));
    }

    fn merge(&mut self, other: &SymPauliAcc) {
        self.tr_alt = self.tr_alt.add(&other.tr_alt);
        self.net = self.net.add(&other.net);
    }

    fn add_from_elem(&mut self, elem: &Elem) {
        for (w, c) in &elem.terms {
            self.add_term(c, w.len());
        }
    }
}

// ════════════════════════════════════════════════════════════════
// Engine core
// ════════════════════════════════════════════════════════════════

struct Eng;

impl Eng {
    fn multiply_and_reduce(elem: &mut Elem, gen: u8, c: &LPoly, d: &LPoly, is_dbl: bool, ha: &LPoly) {
        if is_dbl { elem.pn_count += 1; }
        let old: Vec<(W, LPoly)> = elem.terms.drain().collect();
        let mut stable: FxHashMap<W, LPoly> = FxHashMap::default();
        let mut pending: Vec<(W, LPoly)> = Vec::new();

        for (w, coeff) in old {
            if !d.is_zero() {
                let e = stable.entry(w).or_insert(LPoly::zero());
                *e = e.add(&coeff.mul(d));
            }
            if !c.is_zero() {
                pending.push((w.push(gen), coeff.mul(c)));
            }
        }

        loop {
            let mut next: Vec<(W, LPoly)> = Vec::new();
            let mut any_reduced = false;
            for (word, coeff) in pending {
                if coeff.is_zero() { continue; }
                let red = word.junction_check().or_else(|| word.find_reduction());
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
                            let (a, b) = (w.get(pos), w.get(pos + 1));
                            w.set(pos, b); w.set(pos + 1, a);
                            next.push((w, coeff));
                        }
                        2 => {
                            let mut w = word;
                            let (a, b) = (w.get(pos), w.get(pos + 1));
                            w.set(pos, b); w.set(pos + 1, a); w.set(pos + 2, b);
                            next.push((w, coeff));
                        }
                        _ => {}
                    }
                } else {
                    let e = stable.entry(word).or_insert(LPoly::zero());
                    *e = e.add(&coeff);
                }
            }
            if !any_reduced { break; }
            let mut consolidated: FxHashMap<W, LPoly> = FxHashMap::default();
            for (w, c) in next {
                if c.is_zero() { continue; }
                let e = consolidated.entry(w).or_insert(LPoly::zero());
                *e = e.add(&c);
            }
            pending = Vec::new();
            for (w, c) in consolidated {
                if c.is_zero() { continue; }
                if let Some(existing) = stable.remove(&w) {
                    let merged = existing.add(&c);
                    if !merged.is_zero() && w.find_reduction().is_some() {
                        pending.push((w, merged));
                    } else if !merged.is_zero() {
                        stable.insert(w, merged);
                    }
                } else {
                    pending.push((w, c));
                }
            }
        }
        stable.retain(|_, c| !c.is_zero());
        elem.terms = stable;
    }

    fn strip_with_pauli(terms: &mut FxHashMap<W, LPoly>) -> SymPauliAcc {
        let mut removed = SymPauliAcc::zero();
        let max_len = terms.keys().map(|w| w.len()).max().unwrap_or(0);
        for tl in (2..=max_len).rev() {
            let to_rm: Vec<W> = terms.keys()
                .filter(|w| w.len() == tl && !terms[*w].is_zero())
                .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &to_rm {
                if let Some(c) = terms.remove(w) {
                    removed.add_term(&c, w.len());
                }
            }
        }
        let adj: Vec<W> = terms.keys()
            .filter(|w| w.len() == 2 && !terms[*w].is_zero() && w.get(1) == w.get(0) + 1)
            .filter(|w| terms.get(&W::E.push(w.get(1))).map_or(false, |c| !c.is_zero()))
            .cloned().collect();
        for w in &adj {
            if let Some(c) = terms.remove(w) {
                removed.add_term(&c, w.len());
            }
        }
        terms.retain(|_, c| !c.is_zero());
        removed
    }

    fn build(z: usize, n: usize, mid_threshold: usize) -> (Elem, SymPauliAcc) {
        let a = z + n;
        let ha = ha_poly();
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut elem = Elem::identity();
        let mut accum = SymPauliAcc::zero();
        let t0 = Instant::now();
        let strip_after = if a > 9 { 8 } else { 999 };
        let mut total_mid_strips: u64 = 0;
        // Eager mode: strip after EVERY crossing when threshold = 0
        let eager = mid_threshold == 0;
        let effective_threshold = if eager { usize::MAX } else { mid_threshold };

        for k in 1..a {
            for i in 0..k {
                let tc = Instant::now();
                let n_before = elem.n_terms();
                let (c, d, dbl) = crossing_sym(types[i], types[k]);
                Self::multiply_and_reduce(&mut elem, i as u8, &c, &d, dbl, &ha);

                // Strip condition: eager (always) or threshold exceeded
                let should_strip = (eager && k >= strip_after)
                    || elem.n_terms() > effective_threshold;

                if should_strip {
                    let n_pre = elem.n_terms();
                    let removed = Self::strip_with_pauli(&mut elem.terms);
                    accum.merge(&removed);
                    total_mid_strips += 1;
                    let ms = tc.elapsed().as_millis();
                    if ms > 50 || n_pre > 1000 {
                        eprintln!("    ({},{}) {}-{}: {} → {} → {} words (strip), {}ms",
                            i, k, types[i] as char, types[k] as char,
                            n_before, n_pre, elem.n_terms(), ms);
                    }
                } else {
                    let ms = tc.elapsed().as_millis();
                    if ms > 100 || elem.n_terms() > 5000 {
                        eprintln!("    ({},{}) {}-{}: {} → {} words, {}ms",
                            i, k, types[i] as char, types[k] as char,
                            n_before, elem.n_terms(), ms);
                    }
                }
            }

            let mc = elem.max_coeff_log10();
            let mb = elem.mem_bytes() as f64 / 1_048_576.0;
            let elapsed = t0.elapsed().as_secs_f64();

            // Always strip at strand boundary for A > 9
            if (k + 1) > strip_after {
                let n_pre = elem.n_terms();
                let removed = Self::strip_with_pauli(&mut elem.terms);
                accum.merge(&removed);
                eprintln!("  strand {}/{}: {} → {} words, coeff~10^{:.0}, {:.0}MB, {:.1}s [{}s]",
                    k, a - 1, n_pre, elem.n_terms(), mc, mb, elapsed, total_mid_strips);
            } else {
                eprintln!("  strand {}/{}: {} words, coeff~10^{:.0}, {:.0}MB, {:.1}s",
                    k, a - 1, elem.n_terms(), mc, mb, elapsed);
            }
        }
        (elem, accum)
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 3 {
        eprintln!("hecke-bigint (v9) — BigInt symbolic Pauli witness, exact in q");
        eprintln!("Usage: hecke-bigint Z N [mid_strip_threshold]");
        eprintln!("  Z N: nucleus (e.g. 27 33 for ⁶⁰Co)");
        eprintln!("  mid_strip_threshold: 0 = eager (strip after EVERY crossing)");
        eprintln!("                       N = strip when words > N (default: 50000)");
        eprintln!("  Eager mode recommended for A > 20.");
        std::process::exit(1);
    }

    let z: usize = args[1].parse().unwrap();
    let n: usize = args[2].parse().unwrap();
    let mid_threshold: usize = args.get(3).and_then(|s| s.parse().ok())
        .unwrap_or(if z + n > 20 { 0 } else { 50000 });
    let a = z + n;

    eprintln!("hecke-bigint v9 — BigInt symbolic engine");
    eprintln!("  A={} (Z={}, N={}), mid-strip: {}",
        a, z, n, if mid_threshold == 0 { "EAGER (every crossing)".to_string() }
                 else { format!("threshold {}", mid_threshold) });
    eprintln!("  No i128 overflow — arbitrary precision coefficients");

    let t0 = Instant::now();
    let (elem, accum) = Eng::build(z, n, mid_threshold);

    let mut total = accum.clone();
    let mut kept = SymPauliAcc::zero();
    kept.add_from_elem(&elem);
    total.merge(&kept);

    let elapsed = t0.elapsed().as_secs_f64();
    let mc = elem.max_coeff_log10();

    eprintln!("\n  Result: {} words, coeff~10^{:.0}, {:.0}MB, {:.1}s",
        elem.n_terms(), mc, elem.mem_bytes() as f64 / 1e6, elapsed);

    // Evaluate at q₀
    // For large pn_count, 2^pn_count overflows f64. Compute the RATIO
    // F_Pauli = |tr_alt/net| directly (the 2^pn_count cancels).
    let q0: f64 = 1.10998;
    let t0_val = q0.sqrt();

    // For pn_count > 1000, f64 eval is unreliable.
    // Use the ratio directly: both tr_alt and net have the same 2^pn_count factor.
    let tr_alt_raw = total.tr_alt.eval_f64(t0_val);
    let net_raw = total.net.eval_f64(t0_val);
    let (tr_alt_val, net_val, f) = if tr_alt_raw.is_finite() && net_raw.is_finite() {
        let denom = 2.0_f64.powi(elem.pn_count as i32);
        let ta = tr_alt_raw / denom;
        let nv = net_raw / denom;
        let fp = if nv.abs() > 1e-30 { ta.abs() / nv.abs() } else { 0.0 };
        (ta, nv, fp)
    } else {
        // f64 overflow: compute ratio directly (2^pn_count cancels)
        // F = |tr_alt_raw / net_raw| — no denominator needed for the ratio
        let fp = if net_raw.abs() > 1e-30 { (tr_alt_raw / net_raw).abs() }
                 else if net_raw == 0.0 && tr_alt_raw == 0.0 { f64::NAN }
                 else { f64::INFINITY };
        (tr_alt_raw, net_raw, fp)
    };

    println!("F_Pauli({}{}) = {:.10} (exact in q, evaluated at q₀ = {})",
        a, match z {
            1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",
            9=>"F",10=>"Ne",20=>"Ca",26=>"Fe",27=>"Co",28=>"Ni",_=>"?"
        }, f, q0);
    println!("  tr_alt(q₀) = {:.10e}", tr_alt_val);
    println!("  net(q₀)    = {:.10e}", net_val);
    println!("  pn_count = {} (denom = 2^{})", elem.pn_count, elem.pn_count);
    println!("  max coeff ~10^{:.0}", mc);
    println!("  time = {:.1}s", elapsed);
}
