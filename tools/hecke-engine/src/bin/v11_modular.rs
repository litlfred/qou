// v11: Minimal modular f_pauli engine.
// Direct port of v9's NF computation with u64 mod p coefficients.
// ONLY computes f_pauli = |tr_alt/net| — no full polynomial output.
// For A ≤ 12: exact (coefficients fit in u64).
// For A > 12: use multiple primes + CRT.

use rustc_hash::FxHashMap;
use std::collections::BTreeMap;
use std::time::Instant;

const P: u64 = 1_000_000_007;
fn ma(a: u64, b: u64) -> u64 { ((a as u128 + b as u128) % P as u128) as u64 }
fn ms(a: u64, b: u64) -> u64 { if a >= b { a - b } else { P - b + a } }
fn mm(a: u64, b: u64) -> u64 { ((a as u128 * b as u128) % P as u128) as u64 }

// Laurent polynomial mod P
#[derive(Clone)]
struct L { t: BTreeMap<i32, u64> }
impl L {
    fn zero() -> Self { Self { t: BTreeMap::new() } }
    fn one() -> Self { let mut m = Self::zero(); m.t.insert(0, 1); m }
    fn is_zero(&self) -> bool { self.t.is_empty() }
    fn n(&self) -> usize { self.t.len() }
    fn add(&self, o: &L) -> L {
        let mut r = self.t.clone();
        for (k, v) in &o.t {
            let e = r.entry(*k).or_insert(0);
            *e = ma(*e, *v);
            if *e == 0 { r.remove(k); }
        }
        L { t: r }
    }
    fn sub(&self, o: &L) -> L {
        let mut r = self.t.clone();
        for (k, v) in &o.t {
            let e = r.entry(*k).or_insert(0);
            *e = ms(*e, *v);
            if *e == 0 { r.remove(k); }
        }
        L { t: r }
    }
    fn mul(&self, o: &L) -> L {
        let mut r: BTreeMap<i32, u64> = BTreeMap::new();
        for (k1, v1) in &self.t {
            for (k2, v2) in &o.t {
                let k = k1 + k2;
                let e = r.entry(k).or_insert(0);
                *e = ma(*e, mm(*v1, *v2));
                if *e == 0 { r.remove(&k); }
            }
        }
        L { t: r }
    }
    fn scale_sign(&self, neg: bool) -> L {
        if !neg { return self.clone(); }
        let mut r = BTreeMap::new();
        for (k, v) in &self.t { r.insert(*k, ms(0, *v)); }
        L { t: r }
    }
    fn shift(&self, s: i32) -> L {
        let mut r = BTreeMap::new();
        for (k, v) in &self.t { r.insert(k + s, *v); }
        L { t: r }
    }
    fn eval_f64(&self, t: f64) -> f64 {
        let hp = P / 2;
        self.t.iter().map(|(&k, &v)| {
            let c = if v > hp { -((P - v) as f64) } else { v as f64 };
            c * t.powi(k)
        }).sum()
    }
}

// Word: same as v9 (u128 packed, 4 words)
#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct W { d: [u128; 4], n: u8 }
impl W {
    const E: W = W { d: [0; 4], n: 0 };
    fn len(self) -> usize { self.n as usize }
    fn get(self, i: usize) -> u8 { ((self.d[i/16] >> ((i%16)*8)) & 0xFF) as u8 }
    fn set(&mut self, i: usize, v: u8) {
        self.d[i/16] &= !(0xFF << ((i%16)*8));
        self.d[i/16] |= (v as u128) << ((i%16)*8);
    }
    fn push(mut self, v: u8) -> W {
        if self.n >= 64 { return self; }
        let i = self.n as usize; self.set(i, v); self.n += 1; self
    }
    fn remove_at(self, pos: usize) -> W {
        let mut r = W::E;
        for i in 0..self.len() { if i != pos { r = r.push(self.get(i)); } }
        r
    }
    fn drop_last(self) -> W {
        let mut r = self;
        let i = (r.n - 1) as usize;
        r.set(i, 0);  // zero the byte for correct hash/eq
        r.n -= 1; r
    }
    fn junction(self) -> Option<(usize, u8)> {
        let n = self.len(); if n < 2 { return None; }
        let p = n - 2; let (a, b) = (self.get(p), self.get(p+1));
        if a == b { return Some((p, 0)); }
        if n >= 3 { let c = self.get(p-1);
            if c == b && (a as i8 - c as i8).unsigned_abs() == 1 { return Some((p-1, 2)); } }
        if (a as i8 - b as i8).unsigned_abs() >= 2 && a > b { return Some((p, 1)); }
        None
    }
    fn find_red(self) -> Option<(usize, u8)> {
        let n = self.len();
        for p in 0..n.saturating_sub(1) {
            let (a, b) = (self.get(p), self.get(p+1));
            if a == b { return Some((p, 0)); }
            if p+2 < n { let c = self.get(p+2);
                if a == c && (a as i8 - b as i8).unsigned_abs() == 1 {
                    if (b,a,b) < (a,b,a) { return Some((p, 2)); } } }
            if (a as i8 - b as i8).unsigned_abs() >= 2 && a > b { return Some((p, 1)); }
        }
        None
    }
}

fn ha() -> L { let mut h = L::zero(); h.t.insert(2, 1); h.t.insert(-2, P-1); h }

fn crossing(ti: u8, tj: u8) -> (L, L, bool) {
    let h = ha();
    match (ti, tj) {
        (b'p', b'p') => (L::one(), L::zero(), false),
        (b'n', b'n') => {
            let mut d = L::zero(); d.t.insert(2, P-1); d.t.insert(-2, 1); // -HA
            (L::one(), d, false)
        }
        _ => { let mut c = L::zero(); c.t.insert(0, 2);
               let mut d = L::zero(); d.t.insert(2, P-1); d.t.insert(-2, 1);
               (c, d, true) }
    }
}

fn mul_reduce(terms: &mut FxHashMap<W, L>, gen: u8, c: &L, d: &L, h: &L) {
    let old: Vec<(W, L)> = terms.drain().collect();
    let mut stable: FxHashMap<W, L> = FxHashMap::default();
    let mut pending: Vec<(W, L)> = Vec::new();
    for (w, co) in old {
        if !d.is_zero() { let e = stable.entry(w).or_insert(L::zero()); *e = e.add(&co.mul(d)); }
        if !c.is_zero() { pending.push((w.push(gen), co.mul(c))); }
    }
    for _ in 0..500000 {
        let mut next: Vec<(W, L)> = Vec::new();
        let mut any = false;
        for (w, co) in pending {
            if co.is_zero() { continue; }
            let red = w.junction().or_else(|| w.find_red());
            if let Some((pos, rule)) = red {
                any = true;
                match rule {
                    0 => { let w1 = w.remove_at(pos+1); let w2 = w1.remove_at(pos);
                           next.push((w1, co.mul(h))); next.push((w2, co)); }
                    1 => { let mut ww = w; let (a,b) = (ww.get(pos), ww.get(pos+1));
                           ww.set(pos, b); ww.set(pos+1, a); next.push((ww, co)); }
                    2 => { let mut ww = w; let (a,b) = (ww.get(pos), ww.get(pos+1));
                           ww.set(pos, b); ww.set(pos+1, a); ww.set(pos+2, b);
                           next.push((ww, co)); }
                    _ => {}
                }
            } else { let e = stable.entry(w).or_insert(L::zero()); *e = e.add(&co); }
        }
        if !any { break; }
        let mut cons: FxHashMap<W, L> = FxHashMap::default();
        for (w, c) in next { if c.is_zero() { continue; }
            let e = cons.entry(w).or_insert(L::zero()); *e = e.add(&c); }
        pending = Vec::new();
        for (w, c) in cons { if c.is_zero() { continue; }
            if let Some(ex) = stable.remove(&w) {
                let m = ex.add(&c);
                if !m.is_zero() && w.find_red().is_some() { pending.push((w, m)); }
                else if !m.is_zero() { stable.insert(w, m); }
            } else { pending.push((w, c)); } }
    }
    stable.retain(|_, c| !c.is_zero());
    *terms = stable;
}

// Pauli accumulator: same formula as v9
fn accumulate(terms: &FxHashMap<W, L>) -> (L, L) {
    let mut tr_alt = L::zero();
    let mut net = L::zero();
    for (w, c) in terms {
        net = net.add(c);
        let wl = w.len() as i32;
        let neg = wl % 2 != 0;
        tr_alt = tr_alt.add(&c.scale_sign(neg).shift(-2 * wl));
    }
    (tr_alt, net)
}

fn strip(terms: &mut FxHashMap<W, L>) -> (L, L) {
    let mut alt = L::zero(); let mut net = L::zero();
    for _ in 0..500 {
        let mut any = false;
        let ml = terms.keys().map(|w| w.len()).max().unwrap_or(0);
        for tl in (2..=ml).rev() {
            let rm: Vec<W> = terms.keys()
                .filter(|w| w.len() == tl && !terms[*w].is_zero())
                .filter(|w| terms.get(&w.drop_last()).map_or(false, |c| !c.is_zero()))
                .cloned().collect();
            for w in &rm {
                if let Some(c) = terms.remove(w) {
                    let wl = w.len() as i32;
                    let neg = wl % 2 != 0;
                    alt = alt.add(&c.scale_sign(neg).shift(-2 * wl));
                    net = net.add(&c);
                    any = true;
                }
            }
        }
        if !any { break; }
    }
    terms.retain(|_, c| !c.is_zero());
    (alt, net)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let z: usize = args.get(1).and_then(|s| s.parse().ok()).unwrap_or(2);
    let n: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(2);
    let a = z + n;
    let h = ha();
    let mut types = vec![b'p'; z]; types.extend(vec![b'n'; n]);
    let mut terms: FxHashMap<W, L> = FxHashMap::default();
    terms.insert(W::E, L::one());
    let mut pn: u32 = 0;
    let mut acc_alt = L::zero(); let mut acc_net = L::zero();
    let t0 = Instant::now();

    for k in 1..a {
        for i in 0..k {
            let (c, d, dbl) = crossing(types[i], types[k]);
            if dbl { pn += 1; }
            mul_reduce(&mut terms, i as u8, &c, &d, &h);
            if a > 16 || terms.len() > 50000 {
                let (ta, tn) = strip(&mut terms);
                acc_alt = acc_alt.add(&ta); acc_net = acc_net.add(&tn);
            }
        }
        if a > 12 {
            let (ta, tn) = strip(&mut terms);
            acc_alt = acc_alt.add(&ta); acc_net = acc_net.add(&tn);
        }
        eprintln!("  strand {}/{}: {} words, {:.1}s", k, a-1, terms.len(), t0.elapsed().as_secs_f64());
    }
    // Final strip
    let (ta, tn) = strip(&mut terms);
    acc_alt = acc_alt.add(&ta); acc_net = acc_net.add(&tn);
    // Add remaining
    let (ra, rn) = accumulate(&terms);
    acc_alt = acc_alt.add(&ra); acc_net = acc_net.add(&rn);

    let elapsed = t0.elapsed().as_secs_f64();
    let t_val = 1.10998_f64.sqrt();
    let div = 2.0_f64.powi(pn as i32);
    let alt_f = acc_alt.eval_f64(t_val) / div;
    let net_f = acc_net.eval_f64(t_val) / div;
    let fp = if net_f.abs() > 1e-30 { (alt_f / net_f).abs() } else { 0.0 };

    let sym = match z { 1=>"h",2=>"he",3=>"li",4=>"be",5=>"b",6=>"c",7=>"n",8=>"o",
        9=>"f",10=>"ne",11=>"na",12=>"mg",13=>"al",14=>"si",15=>"p",16=>"s",
        17=>"cl",18=>"ar",19=>"k",20=>"ca",_=>"?" };
    println!("f_pauli({}{}) = {:.10}", a, sym, fp);
    println!("  tr_alt = {:.10e}, net = {:.10e}", alt_f, net_f);
    println!("  {} words, pn={}, {:.2}s", terms.len(), pn, elapsed);

    // Write minimal cert
    let cert = serde_json::json!({
        "isotope": {"z": z, "n": n, "a": a, "symbol": sym},
        "engine": {"name": "hecke-modular", "version": "0.11.0"},
        "f_pauli_f64": fp, "tr_alt_f64": alt_f, "net_f64": net_f,
        "elapsed_seconds": elapsed,
    });
    let fname = format!("certificate-{}{}.json", a, sym);
    std::fs::write(&fname, serde_json::to_string_pretty(&cert).unwrap()).unwrap();
    eprintln!("  Certificate: {}", fname);
}
