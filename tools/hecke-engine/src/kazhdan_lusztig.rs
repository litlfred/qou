use std::collections::HashMap;

#[derive(Clone, Copy, PartialEq, Eq, Hash, Debug)]
pub struct Perm(u64);

impl Perm {
    pub fn new(n: usize, elements: &[u8]) -> Self {
        let mut val = 0u64;
        for &e in elements {
            val = (val << 4) | (e as u64);
        }
        Perm(val)
    }

    pub fn to_vec(&self, n: usize) -> Vec<u8> {
        let mut res = Vec::with_capacity(n);
        let mut val = self.0;
        for _ in 0..n {
            res.push((val & 0xF) as u8);
            val >>= 4;
        }
        res.reverse();
        res
    }

    pub fn identity(n: usize) -> Self {
        let mut elements = Vec::with_capacity(n);
        for i in 0..n {
            elements.push((i + 1) as u8);
        }
        Self::new(n, &elements)
    }

    pub fn apply_simple_reflection(&self, n: usize, i: usize) -> Self {
        let shift1 = 4 * (n - 1 - i);
        let shift2 = 4 * (n - 2 - i);
        let val1 = (self.0 >> shift1) & 0xF;
        let val2 = (self.0 >> shift2) & 0xF;
        let mask1 = 0xF << shift1;
        let mask2 = 0xF << shift2;
        let mut val = self.0 & !mask1 & !mask2;
        val |= val2 << shift1;
        val |= val1 << shift2;
        Perm(val)
    }

    pub fn right_descent(&self, n: usize) -> Option<usize> {
        let mut val = self.0;
        let mut prev = val & 0xF;
        val >>= 4;
        for i in (0..(n - 1)).rev() {
            let curr = val & 0xF;
            if curr > prev {
                return Some(i);
            }
            prev = curr;
            val >>= 4;
        }
        None
    }

    pub fn has_right_descent(&self, n: usize, i: usize) -> bool {
        let shift1 = 4 * (n - 1 - i);
        let shift2 = 4 * (n - 2 - i);
        let val1 = (self.0 >> shift1) & 0xF;
        let val2 = (self.0 >> shift2) & 0xF;
        val1 > val2
    }

    pub fn length(&self, n: usize) -> usize {
        let mut len = 0;
        let vec = self.to_vec(n);
        for i in 0..n {
            for j in (i + 1)..n {
                if vec[i] > vec[j] {
                    len += 1;
                }
            }
        }
        len
    }
}

pub fn bruhat_le(x: &Perm, w: &Perm, n: usize) -> bool {
    let vx = x.to_vec(n);
    let vw = w.to_vec(n);
    for k in 1..n {
        let mut px = vx[..k].to_vec();
        let mut pw = vw[..k].to_vec();
        px.sort_unstable();
        pw.sort_unstable();
        for j in 0..k {
            if px[j] > pw[j] {
                return false;
            }
        }
    }
    true
}

// A simple polynomial representation: coefficients of q^k.
// max degree is n(n-1)/2, which for n=12 is 66.
// We can use a small Vec or array.
#[derive(Clone, PartialEq, Eq, Debug)]
pub struct Polynomial {
    pub coeffs: Vec<i64>,
}

impl Polynomial {
    pub fn zero() -> Self {
        Polynomial { coeffs: Vec::new() }
    }

    pub fn one() -> Self {
        Polynomial { coeffs: vec![1] }
    }

    pub fn is_zero(&self) -> bool {
        self.coeffs.is_empty()
    }

    pub fn add(&self, other: &Polynomial) -> Polynomial {
        let mut res = Vec::with_capacity(self.coeffs.len().max(other.coeffs.len()));
        for i in 0..self.coeffs.len().max(other.coeffs.len()) {
            let a = self.coeffs.get(i).copied().unwrap_or(0);
            let b = other.coeffs.get(i).copied().unwrap_or(0);
            res.push(a + b);
        }
        while res.last() == Some(&0) {
            res.pop();
        }
        Polynomial { coeffs: res }
    }

    pub fn sub(&self, other: &Polynomial) -> Polynomial {
        let mut res = Vec::with_capacity(self.coeffs.len().max(other.coeffs.len()));
        for i in 0..self.coeffs.len().max(other.coeffs.len()) {
            let a = self.coeffs.get(i).copied().unwrap_or(0);
            let b = other.coeffs.get(i).copied().unwrap_or(0);
            res.push(a - b);
        }
        while res.last() == Some(&0) {
            res.pop();
        }
        Polynomial { coeffs: res }
    }

    pub fn mul_q_power(&self, power: usize) -> Polynomial {
        if self.is_zero() {
            return self.clone();
        }
        let mut res = vec![0; power];
        res.extend_from_slice(&self.coeffs);
        Polynomial { coeffs: res }
    }

    pub fn scale(&self, scalar: i64) -> Polynomial {
        if scalar == 0 {
            return Polynomial::zero();
        }
        let mut res = Vec::with_capacity(self.coeffs.len());
        for &c in &self.coeffs {
            res.push(c * scalar);
        }
        Polynomial { coeffs: res }
    }

    pub fn eval_at_1(&self) -> i64 {
        self.coeffs.iter().sum()
    }
}

pub struct KLContext {
    n: usize,
    cache: HashMap<(Perm, Perm), Polynomial>,
    perms: Vec<Perm>,
}

impl KLContext {
    pub fn new(n: usize) -> Self {
        // Generate permutations
        let mut perms = Vec::new();
        let mut current: Vec<u8> = (1..=(n as u8)).collect();
        // Heap's algorithm
        fn generate(k: usize, arr: &mut [u8], perms: &mut Vec<Perm>, n: usize) {
            if k == 1 {
                perms.push(Perm::new(n, arr));
            } else {
                generate(k - 1, arr, perms, n);
                for i in 0..(k - 1) {
                    if k % 2 == 0 {
                        arr.swap(i, k - 1);
                    } else {
                        arr.swap(0, k - 1);
                    }
                    generate(k - 1, arr, perms, n);
                }
            }
        }
        generate(n, &mut current, &mut perms, n);

        KLContext {
            n,
            cache: HashMap::new(),
            perms,
        }
    }

    pub fn kl_polynomial(&mut self, x: Perm, w: Perm) -> Polynomial {
        if x == w {
            return Polynomial::one();
        }
        if !bruhat_le(&x, &w, self.n) {
            return Polynomial::zero();
        }
        
        if let Some(res) = self.cache.get(&(x, w)) {
            return res.clone();
        }

        let s = w.right_descent(self.n).unwrap();
        let ws = w.apply_simple_reflection(self.n, s);
        let xs = x.apply_simple_reflection(self.n, s);
        
        let x_has_s_descent = x.has_right_descent(self.n, s);

        let mut c;
        if x_has_s_descent {
            let pxsws = self.kl_polynomial(xs, ws);
            let pxws = self.kl_polynomial(x, ws);
            c = pxsws.add(&pxws.mul_q_power(1));
        } else {
            let pxsws = self.kl_polynomial(xs, ws);
            let pxws = self.kl_polynomial(x, ws);
            c = pxsws.mul_q_power(1).add(&pxws);
        }

        let lw = w.length(self.n);
        let mut correction = Polynomial::zero();
        
        for i in 0..self.perms.len() {
            let z = self.perms[i];
            if !z.has_right_descent(self.n, s) { continue; }
            if z == ws { continue; }
            let lz = z.length(self.n);
            if lw < lz { continue; }
            if (lw - lz) % 2 != 0 { continue; }
            if !bruhat_le(&z, &ws, self.n) { continue; }
            if !bruhat_le(&x, &z, self.n) { continue; }
            
            let p_z_ws = self.kl_polynomial(z, ws);
            let diff = lw - lz;
            let target_power = (diff - 1) / 2;
            let mu = p_z_ws.coeffs.get(target_power).copied().unwrap_or(0);
            
            if mu != 0 {
                let p_x_z = self.kl_polynomial(x, z);
                let term = p_x_z.scale(mu).mul_q_power(diff / 2);
                correction = correction.add(&term);
            }
        }

        let result = c.sub(&correction);
        self.cache.insert((x, w), result.clone());
        result
    }
}
