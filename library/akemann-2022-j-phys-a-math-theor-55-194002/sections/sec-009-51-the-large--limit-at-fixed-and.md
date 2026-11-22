---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-009-51-the-large--limit-at-fixed-and
section_title: "The large- limit at fixed and"
section_number: 5.1
pages: 21-24
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
In the asymptotic large-n limit of the χGUE at the hard edge, with our convention of an n-
independent weight function, it is well known that the eigenvalues, and therefore also the
spacings and masses scale with √n, see [18]. We therefore define the following variables
σ ≡√n s,
μ f ≡√n m f,
f = 1, . . . , Nf,
(76)
20
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
where σ and the μ f remain finite in the large-n limit. In view of the integrations to be performed
in (73), and the definition (61) of the shifted variables therein, we also redefine the integration
variables in the following fashion:
χ ≡√n xk
and
λ j ≡√n x j,
j = 1, . . . , k −1.
(77)
We begin with the large-n asymptotic of the generalised Laguerre polynomials, using
[40, equation (18.15.19)]
lim
n, j→∞
j/n→t
1
nν L(ν)
j
	
−z2
n

=
	√t
z

ν
Iν

2z
√
t

,
(78)
with Iν(z) the modified Bessel function of the first kind. In foresight, we already allow here for
a general degree j of the polynomial, to be able to take the limit under the sum in (71). When
j = O(n) we can set t = 1 in the above expression, as it will be the case for the unintegrated
Laguerre polynomials. We apply this first to the mass dependent determinant of Laguerre poly-
nomials in the denominator in the first line of (73). In view of the scaling (76), we also include
the mass dependent pre-factor Nf
f=1m2ν
f into the determinant, to obtain
lim
n→∞det

(μ2
a/n)ν+b−1L(ν+b−1)
n
(−μ2
a/n)

a,b=1,...,Nf
= det

μν+b−1
a
Iν+b−1(2μa)

a,b=1,...,Nf.
(79)
Next, we move to the building blocks of the large determinant in the last line of (73). We begin
with distinguishing the Laguerre polynomials of different variables, multiplied by different
powers. Inserting equations (76) and (77), we obtain from the limit (78)
#s2(d−a)L(d−a+2)
n+a−2 (−#s2) =
	χ + σ
√n

2(d−a)
L(d−a+2)
n+a−2
	
−(χ + σ)2
n

≈n2(χ + σ)d−a−2Id−a+2(2(χ + σ)),
#m2d−2
b
L(d+1)
n−1 (−#m2
b) ≈n2[(χ + σ)2 + μ2
b](d−3)/2Id+1
	
2
"
(χ + σ)2 + μ2
b

,
b = 1, . . . , Nf,
#x2d−2
c
L(d+1)
n−1 (−#x2
c) ≈n2[(χ + σ)2 −λ2
c](d−3)/2Id+1
	
2
"
(χ + σ)2 −λ2c

,
c = 1, . . . , k −1,
#x2d−2
c
L(d+1)
n−1 (−#x2
c) ≈n2[σ(2χ + σ)](d−3)/2Id+1

2

σ(2χ + σ)

,
c = k.
(80)
In view of these results, it is convenient to define again a set of limiting shifted variables, in
analogy to (61), in order to compactify the final answer for the limiting spacing distribution:
#σ ≡χ + σ = √n#s,
#μ f ≡
"
(χ + σ)2 + μ2
f = √n #m f,
f = 1, . . . , Nf,
#χ ≡

σ(2χ + σ) = √n #xk,
#λc ≡

(χ + σ)2 −λ2c = √n #xc,
c = 1, . . . , k −1.
(81)
21
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
We are now ready to take the limit of the kernel (71). For any e = 1, . . . , k −1, it holds
#K(a−1)
2,n−1(−#s2, −#x2
e) ≈
2
na−1
n−2
'
j=0
ja−3
	#σ2
n

1−a
L(3−a)
j+a−1
	
−#σ2
n

L(2)
j

−
#λ2
e
n

≈2n3
 1
0
dt t
a−1
2 #σ−1−aI3−a

2#σ
√
t
 #λ−2
e I2

2#λe
√
t

= n3Ka−1

#σ, #λe

,
(82)
where we have defined
Ka−1

#σ, #λe

≡4#σ−1−a#λ−2
e
 1
0
dT TaI3−a (2#σT) I2(2#λeT),
(83)
after changing variables. The same result holds for e = k, replacing #λe by #χ. Finally, for a = 1
we obtain for the limit of the χGUE kernel:
#K(0)
2,n−1(−#m2
b, −#x2
e) ≈n3K0

#μb, #λe

= n34#μ−2
b #λ−2
e
 1
0
dT TI2 (2#μbT) I2(2#λeT)
=
4n3
(#μb#λe)2(#λ2e −#μ2
b)

2#λeI1(2#λe)I2(2#μb) −2#μbI1(2#μb)I2(2#λe)

,
(84)
for b = 1, . . . , Nf and e = 1, . . . , k −1, and likewise for different arguments #μb →#λc and
#λe →#χ. In the last step we have performed the integral, corresponding to the limit of the sec-
ond line in (49), whereas the first line follows from replacing the sum with an integral. Finally,
for equal arguments we have
#K(0)
2,n−1(−#x2
c, −#x2
c) ≈n3K0

#λc, #λc

= n3 2
#λ4c

I2(2#λc)2 −I3(2#λc)I1(2#λc)

,
(85)
and likewise for #λc →#χ. If we had taken the limit for Laguerre polynomials with positive
argument in (78), this would be proportional to the Bessel density at ν = 2, see (9). The factor
of two in the argument of the Bessel functions indicates that in our scaling limit (85) the mean
level spacing is π/2. We will come back to this below.
We now have all ingredients together to take the limit of the spacing distribution (73), where
in view of the scaling (76) we define
(86)
22
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
In the quenched case Nf = 0 of the χGUE with ν = 0 it reduces to
(87)
In the simplest case k = 1 (spacing between the first and second smallest eigenvalue), we thus
obtain the following single integral representation
p(0,0)
1
(σ) = 4
 ∞
0
dχ χ(χ + σ)e−(χ+σ)2 	
I2

2

σ(2χ + σ)
2
−I3

2

σ(2χ + σ)

I1

2

σ(2χ + σ)

,
(88)
where we have spelled out all shifted variables explicitly, as well as the kernel from (85).
As explained at the end of section 3, we still have to unfold, by computing the first
moment and rescaling the spacing distribution accordingly. Here and in the setting with more
parameters, we were only able to do this numerically. In the present case this means
¯σ1 =
 ∞
0
dσ σp(0,0)
1
(σ) ≈1.509,
(89)
leading to the final answer
¯p(0,0)
1
(σ) = ¯σ1p(0,0)
1
(¯σ1σ).
(90)
As it was argued after (85), the approximatemean level spacing we expect here is π/2 ≈1.571.
It is very close to ¯σ1, but given the very small deviation from the bulk spacing to be discussed
below, we better use its exact value ¯σ1 to set the first moment of ¯p(0,0)
1
(σ) exactly to unity.
