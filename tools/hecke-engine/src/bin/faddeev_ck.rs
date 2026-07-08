use num_rational::Ratio;
use num_traits::Zero;
use std::fmt;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct QSqrt3 {
    a: Ratio<i128>,
    b: Ratio<i128>,
}

impl QSqrt3 {
    fn new(a: Ratio<i128>, b: Ratio<i128>) -> Self { Self { a, b } }
    fn zero() -> Self { Self::new(Ratio::zero(), Ratio::zero()) }
    fn one() -> Self { Self::new(Ratio::new(1, 1), Ratio::zero()) }
    fn is_zero(&self) -> bool { self.a.is_zero() && self.b.is_zero() }

    fn add(self, rhs: Self) -> Self { Self::new(self.a + rhs.a, self.b + rhs.b) }
    fn sub(self, rhs: Self) -> Self { Self::new(self.a - rhs.a, self.b - rhs.b) }
    fn mul(self, rhs: Self) -> Self {
        let a = self.a * rhs.a + Ratio::new(3, 1) * self.b * rhs.b;
        let b = self.a * rhs.b + self.b * rhs.a;
        Self::new(a, b)
    }
    fn div(self, rhs: Self) -> Self {
        let denom = rhs.a * rhs.a - Ratio::new(3, 1) * rhs.b * rhs.b;
        assert!(!denom.is_zero(), "Division by zero in QSqrt3");
        let a = (self.a * rhs.a - Ratio::new(3, 1) * self.b * rhs.b) / denom;
        let b = (self.b * rhs.a - self.a * rhs.b) / denom;
        Self::new(a, b)
    }
    fn scale(self, r: Ratio<i128>) -> Self {
        Self::new(self.a * r, self.b * r)
    }
}

impl fmt::Display for QSqrt3 {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.is_zero() { return write!(f, "0"); }
        if self.b.is_zero() { return write!(f, "{}", self.a); }
        if self.a.is_zero() {
            if self.b == Ratio::new(1, 1) { return write!(f, "sqrt(3)"); }
            if self.b == Ratio::new(-1, 1) { return write!(f, "-sqrt(3)"); }
            return write!(f, "{}*sqrt(3)", self.b);
        }
        let b_str = if self.b > Ratio::zero() {
            if self.b == Ratio::new(1, 1) { "sqrt(3)".to_string() } else { format!("{}*sqrt(3)", self.b) }
        } else {
            let abs_b = -self.b;
            if abs_b == Ratio::new(1, 1) { "- sqrt(3)".to_string() } else { format!("- {}*sqrt(3)", abs_b) }
        };
        write!(f, "{} {}", self.a, b_str)
    }
}

#[derive(Clone, Debug, PartialEq, Eq)]
struct PSeries {
    coeffs: Vec<QSqrt3>,
}

impl PSeries {
    fn zero(order: usize) -> Self { Self { coeffs: vec![QSqrt3::zero(); order] } }
    
    fn from_const(c: QSqrt3, order: usize) -> Self {
        let mut res = Self::zero(order);
        if order > 0 { res.coeffs[0] = c; }
        res
    }

    fn t(order: usize) -> Self {
        let mut res = Self::zero(order);
        if order > 1 { res.coeffs[1] = QSqrt3::one(); }
        res
    }

    fn add(&self, other: &Self) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        for i in 0..order { res.coeffs[i] = self.coeffs[i].add(other.coeffs[i]); }
        res
    }

    fn sub(&self, other: &Self) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        for i in 0..order { res.coeffs[i] = self.coeffs[i].sub(other.coeffs[i]); }
        res
    }

    fn mul(&self, other: &Self) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        for i in 0..order {
            for j in 0..(order - i) {
                res.coeffs[i + j] = res.coeffs[i + j].add(self.coeffs[i].mul(other.coeffs[j]));
            }
        }
        res
    }

    fn shift_down(&self, n: usize) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        for i in 0..(order - n) {
            res.coeffs[i] = self.coeffs[i + n];
        }
        res
    }

    fn div(&self, other: &Self) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        assert!(!other.coeffs[0].is_zero(), "Division by zero in series");
        let inv_d0 = QSqrt3::one().div(other.coeffs[0]);
        for i in 0..order {
            let mut sum = self.coeffs[i];
            for j in 1..=i {
                sum = sum.sub(res.coeffs[i - j].mul(other.coeffs[j]));
            }
            res.coeffs[i] = sum.mul(inv_d0);
        }
        res
    }

    // Square root of series. r0 is the user-provided square root of coeffs[0]
    fn sqrt(&self, r0: QSqrt3) -> Self {
        let order = self.coeffs.len();
        let mut res = Self::zero(order);
        res.coeffs[0] = r0;
        let inv_2r0 = QSqrt3::one().div(r0.scale(Ratio::new(2, 1)));
        
        for i in 1..order {
            let mut sum = self.coeffs[i];
            for j in 1..i {
                sum = sum.sub(res.coeffs[j].mul(res.coeffs[i - j]));
            }
            res.coeffs[i] = sum.mul(inv_2r0);
        }
        res
    }
    
    // cos(S) where S has 0 constant term
    fn cos(&self) -> Self {
        let order = self.coeffs.len();
        assert!(self.coeffs[0].is_zero());
        let mut res = Self::zero(order);
        res.coeffs[0] = QSqrt3::one(); // cos(0) = 1
        
        let mut term = Self::from_const(QSqrt3::one(), order);
        let s2 = self.mul(self);
        
        let mut sign = Ratio::new(1, 1);
        let mut fact = Ratio::new(1, 1);
        
        for k in 1..order { // actually we only need k up to order/2
            term = term.mul(&s2);
            fact = fact * Ratio::new(1, (2 * k as i128) * (2 * k as i128 - 1));
            sign = -sign;
            
            let c = QSqrt3::new(sign * fact, Ratio::zero());
            for i in 0..order {
                res.coeffs[i] = res.coeffs[i].add(term.coeffs[i].mul(c));
            }
        }
        res
    }
}

fn main() {
    let order = 16;
    let t = PSeries::t(order);
    let mut q = PSeries::zero(order);
    for i in 0..order { q.coeffs[i] = QSqrt3::one(); }
    
    // DNET / COUNIT = [ (1/(1-t))^14 + ... ] / [ (1/(1-t))^4 + ... ] * (1-t)^5 / 2
    let coeffs_dnet = vec![-1, 2, 5, -10, -10, 24, 16, -32, -16, 24, 10, -10, -5, 2, 1];
    let mut num_dnet = PSeries::zero(order);
    let mut q_pow = PSeries::from_const(QSqrt3::one(), order);
    for c in coeffs_dnet {
        let c_q = PSeries::from_const(QSqrt3::new(Ratio::new(c, 1), Ratio::zero()), order);
        num_dnet = num_dnet.add(&c_q.mul(&q_pow));
        q_pow = q_pow.mul(&q);
    }
    let den_dnet = PSeries::from_const(QSqrt3::new(Ratio::new(4, 1), Ratio::zero()), order).mul(&q_pow); // Wait, q_pow needs to be exactly q^7 for the denominator
    
    // Recompute properly:
    // DNET = N(q) / (4 q^7)
    // COUNIT = M(q) / (2 q^2)
    // ratio = N(q) / M(q) * (1 / (2 q^5))
    
    let mut num_dnet = PSeries::zero(order);
    let mut q_pow = PSeries::from_const(QSqrt3::one(), order);
    let coeffs_dnet = vec![-1, 2, 5, -10, -10, 24, 16, -32, -16, 24, 10, -10, -5, 2, 1];
    for c in coeffs_dnet {
        num_dnet = num_dnet.add(&PSeries::from_const(QSqrt3::new(Ratio::new(c, 1), Ratio::zero()), order).mul(&q_pow));
        q_pow = q_pow.mul(&q);
    }
    
    let mut num_counit = PSeries::zero(order);
    let mut q_pow2 = PSeries::from_const(QSqrt3::one(), order);
    let coeffs_counit = vec![1, 2, -2, -2, 1];
    for c in coeffs_counit {
        num_counit = num_counit.add(&PSeries::from_const(QSqrt3::new(Ratio::new(c, 1), Ratio::zero()), order).mul(&q_pow2));
        q_pow2 = q_pow2.mul(&q);
    }
    
    // ratio_t = num_dnet / num_counit * (1 / (2 q^5))
    let mut q5 = PSeries::from_const(QSqrt3::one(), order);
    for _ in 0..5 { q5 = q5.mul(&q); }
    let q5_2 = q5.mul(&PSeries::from_const(QSqrt3::new(Ratio::new(2, 1), Ratio::zero()), order));
    
    // Cancel zeroes at t=0
    let mut num_dnet_shifted = num_dnet.clone();
    let mut num_counit_shifted = num_counit.clone();
    while num_counit_shifted.coeffs[0].is_zero() && num_dnet_shifted.coeffs[0].is_zero() {
        num_counit_shifted = num_counit_shifted.shift_down(1);
        num_dnet_shifted = num_dnet_shifted.shift_down(1);
    }
    
    let ratio_t = num_dnet_shifted.div(&num_counit_shifted).div(&q5_2);
    
    // t -> i t
    // Odd powers get multiplied by i, even powers by (-1)^(k/2).
    // We only want the real part, so we KEEP only the EVEN powers and multiply by (-1)^(k/2).
    let mut real_transformed = PSeries::zero(order);
    for i in (0..order).step_by(2) {
        let sign = if (i / 2) % 2 == 1 { Ratio::new(-1, 1) } else { Ratio::new(1, 1) };
        real_transformed.coeffs[i] = ratio_t.coeffs[i].scale(sign);
    }
    
    // cos_arg = alpha_sub - b_sub * t^2 / 2
    // z_sub = sqrt(q) / (1 + q)
    // Wait, alpha_sub needs sqrt(q).
    // sqrt(q) = sqrt(1 / (1-t))
    let sqrt_q = q.sqrt(QSqrt3::one());
    let q_plus_1 = q.add(&PSeries::from_const(QSqrt3::one(), order));
    let z_sub = sqrt_q.div(&q_plus_1);
    
    // h_sub = q - 1/q = q - (1-t)
    let inv_q = PSeries::from_const(QSqrt3::one(), order).sub(&t);
    let h_sub = q.sub(&inv_q);
    
    // alpha_sub = (z_sub - 1) * h_sub / 2
    let z_minus_1 = z_sub.sub(&PSeries::from_const(QSqrt3::one(), order));
    let alpha_sub = z_minus_1.mul(&h_sub).mul(&PSeries::from_const(QSqrt3::new(Ratio::new(1, 2), Ratio::zero()), order));
    
    // b_sub = sqrt( (h_sub^2 + 3) / (h_sub^2 + 4) )
    let h2 = h_sub.mul(&h_sub);
    let h2_3 = h2.add(&PSeries::from_const(QSqrt3::new(Ratio::new(3, 1), Ratio::zero()), order));
    let h2_4 = h2.add(&PSeries::from_const(QSqrt3::new(Ratio::new(4, 1), Ratio::zero()), order));
    let b2 = h2_3.div(&h2_4);
    
    // sqrt of b2: constant term of b2 is 3/4. So sqrt(3)/2.
    let r0 = QSqrt3::new(Ratio::zero(), Ratio::new(1, 2)); // 0 + 1/2 sqrt(3)
    let b_sub = b2.sqrt(r0);
    
    // b_sub * t^2 / 2
    let t2 = t.mul(&t);
    let t2_2 = t2.mul(&PSeries::from_const(QSqrt3::new(Ratio::new(1, 2), Ratio::zero()), order));
    let b_t2_2 = b_sub.mul(&t2_2);
    
    // cos_arg = alpha_sub - b_t2_2
    let cos_arg = alpha_sub.sub(&b_t2_2);
    
    let cos_base = cos_arg.cos();
    
    let ladder_departure = real_transformed.div(&cos_base);
    
    // Convert raw t^(2k) coefficients to exact c_k (where u = b * t^2 / 2, at t=0 b = sqrt(3)/2, so u = sqrt(3)/4 * t^2)
    // u^k = (sqrt(3)/4)^k * t^(2k). Thus c_k = raw_coeff / (sqrt(3)/4)^k
    let u_scale = QSqrt3::new(Ratio::zero(), Ratio::new(1, 4)); // 0 + 1/4 sqrt(3)
    let mut u_pow = u_scale;
    
    println!("--- Exact algebraic c_k witnesses ---");
    for k in 1..=5 {
        let raw = ladder_departure.coeffs[2 * k];
        let c_k = raw.div(u_pow);
        println!("c_{} = {}", k, c_k);
        u_pow = u_pow.mul(u_scale);
    }
}
