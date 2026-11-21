---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-024-c-model-comparison-for-nonlinear-channel-equalis
section_title: "Model Comparison for Nonlinear Channel Equalisation"
section_number: C
pages: 13-14
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
In Section VI-C we compared the proposed Gaussian kernel
(real- and quaternion-valued) algorithms against strictly-linear
and widely-linear models. The underlying idea is that a novel
nonlinear estimation algorithm is only justiﬁed if it outper-
forms existing (strictly and widely) linear approaches. A com-
pact description of the models implemented in Section VI-C,
together with their optimal least-squares parameters, is given
as follows
• Strictly linear:
ˆxL = As
A = (SHS + ρ1I)−1SHX
S = [s1, . . . , sN ],
• Widely linear:
ˆxW L = Wsa
W =
	
SaHSa + ρ2I

−1SaHX
Sa = [sa
1, . . . , sa
N ],
• Real Gaussian kernel (Eq. (13)):
ˆxRG =
N

i=1
ai K RG(si, s)
[a1, . . . , aN]T = (KHK + ρ3I)−1KHX
Ki, j = K RG(si, s j),
• Quaternion Gaussian kernel (Eq. (14)):
ˆxQG =
N

i=1
bi KQG(si, s)
[b1, . . . , bN]T = (KHK + ρ4I)−1KHX
Ki, j = KQG(si, s j).
Recall that ρ1, ρ2, ρ3, ρ4 > 0 are regularisation factors, and
X = [xT
1 , . . . , xT
N]T is the desired output data.
REFERENCES
[1] V. Vapnik, Estimation of Dependences Based on Empirical Data.
New York, NY, USA: Springer-Verlag, 1982.
[2] J. Xu, Y. Zhou, and Y. Wang, “A classiﬁcation of questions using
SVM and semantic similarity analysis,” in Proc. 6th Int. Conf. Internet
Comput. Sci. Eng., Apr. 2012, pp. 31–34.
[3] I. Guyon, J. Weston, S. Barnhill, and V. Vapnik, “Gene selection for
cancer classiﬁcation using support vector machines,” Mach. Learn.,
vol. 46, nos. 1–3, pp. 389–422, 2002.
[4] J. H. Min and Y.-C. Lee, “Bankruptcy prediction using support vector
machine with optimal choice of kernel function parameters,” Expert Syst.
Appl., vol. 28, no. 4, pp. 603–614, 2005.
[5] B. E. Boser, I. M. Guyon, and V. N. Vapnik, “A training algorithm
for optimal margin classiﬁers,” in Proc. 5th Annu. Workshop Comput.
Learn. Theory, 1992, pp. 144–152.
[6] M. A. Aizerman, E. A. Braverman, and L. Rozoner, “Theoretical
foundations of the potential function method in pattern recognition
learning,” Autom. Remote Control, vol. 25, pp. 821–837, 1964.
[7] H. Drucker, C. Burges, L. Kaufman, A. Smola, and V. Vapnik, “Support
vector regression machines,” in Neural Information Processing Systems.
Cambridge, MA, USA: MIT Press, 1996, pp. 155–161.
[8] N. Cristianini and J. Shawe-Taylor, An Introduction to Support Vector
Machines and Other Kernel-Based Learning Methods. Cambridge, U.K.:
Cambridge Univ. Press, 2000.
[9] B. Scholkopf and A. Smola, Learning With Kernels: Support Vector
Machines, Regularization, Optimization, and Beyond. Cambridge, MA,
USA: MIT Press, 2001.
[10] A. Friedman, Foundations of Modern Analysis, 2nd ed. New York, NY,
USA: Dover, 1982.
[11] N. Aronszajn, “Theory of reproducing kernels,” Trans. Amer. Math. Soc.,
vol. 68, no. 3, pp. 337–404, 1950.
[12] C. Saunders, A. Gammerman, and V. Vovk, “Ridge regression learning
algorithm in dual variables,” in Proc. 15th Int. Conf. Mach. Learn., 1998,
pp. 515–521.
[13] W. Liu, P. P. Pokharel, and J. C. Principe, “The kernel least-mean-square
algorithm,” IEEE Trans. Signal Process., vol. 56, no. 2, pp. 543–554,
Feb. 2008.
[14] C. Richard, J. C. M. Bermudez, and P. Honeine, “Online prediction of
time series data with kernels,” IEEE Trans. Signal Process., vol. 57,
no. 3, pp. 1058–1067, Mar. 2009.
[15] Y. Engel, S. Mannor, and R. Meir, “The kernel recursive least-squares
algorithm,” IEEE Trans. Signal Process., vol. 52, no. 8, pp. 2275–2285,
Aug. 2004.
[16] P. Bouboulis and S. Theodoridis, “The complex Gaussian kernel LMS
algorithm,” in Proc. 20th Int. Conf. Artif. Neural Netw., II, 2010,
pp. 11–20.
[17] P. Bouboulis, S. Theodoridis, and M. Mavroforakis, “The augmented
complex kernel LMS,” IEEE Trans. Signal Process., vol. 60, no. 9,
pp. 4962–4967, Sep. 2012.
[18] F. A. Tobar, A. Kuh, and D. P. Mandic, “A novel augmented complex
valued kernel LMS,” in Proc. 7th IEEE Sensor Array Multichannel
Signal Process. Workshop, Jun. 2012, pp. 473–476.
[19] C. Carmeli, E. de Vito, and A. Toigo, “Vector valued reproducing kernel
Hilbert spaces of integrable functions and Mercer theorem,” Anal. Appl.,
vol. 4, no. 4, pp. 377–408, Oct. 2006.
[20] M. A. Álvarez, L. Rosasco, and N. D. Lawrence, Kernels for Vector-
Valued Functions. Hanover, MA, USA: Now Publishers Inc., 2012.
[21] F. Tobar, S.-Y. Kung, and D. P. Mandic, “Multikernel least mean square
algorithm,” IEEE Trans. Neural Netw. Learn. Syst., vol. 25, no. 2,
pp. 265–277, Feb. 2014.
[22] F. A. Tobar and D. P. Mandic, “Multikernel least squares estimation,”
in Proc. Sensor Signal Process. Defence Conf., Sep. 2012, pp. 1–5.
[23] N. L. Bihan, S. Miron, and J. I. Mars, “MUSIC algorithm for vector-
sensors array using biquaternions,” IEEE Trans. Signal Process., vol. 55,
no. 9, pp. 4523–4533, Sep. 2007.
[24] J. Vía, D. Ramírez, and I. Santamaría, “Properness and widely linear
processing of quaternion random vectors,” IEEE Trans. Inf. Theory,
vol. 56, no. 7, pp. 3502–3515, Jul. 2010.
[25] J. Vía, D. P. Palomar, L. Vielva, and I. Santamaria, “Quaternion ICA
from second-order statistics,” IEEE Trans. Signal Process., vol. 59, no. 4,
pp. 1586–1600, Apr. 2011.
[26] C. C. Took and D. P. Mandic, “Augmented second-order statis-
tics of quaternion random signals,” Signal Process., vol. 91, no. 2,
pp. 214–224, 2011.
[27] J. Navarro-Moreno, R. M. Fernandez-Alcala, and J. C. Ruiz-Molina,
“A quaternion widely linear series expansion and its applications,” IEEE
Signal Process. Lett., vol. 19, no. 12, pp. 868–871, Dec. 2012.
[28] J.
Navarro-Moreno,
R.
M.
Fernández-Alcalá,
C.
C.
Took,
and
D. P. Mandic, “Prediction of wide-sense stationary quaternion random
signals,” Signal Process., vol. 93, no. 9, pp. 2573–2580, 2013.
[29] W. R. Hamilton, “On quaternions; or on a new system of imaginaries
in algebra,” London, Edinburgh Dublin Philosoph. Mag. J. Sci., vol. 25,
no. 163, pp. 10–13, 1844.
[30] D. P. Mandic, C. Jahanchahi, and C. C. Took, “A quaternion gradient
operator and its applications,” IEEE Signal Process. Lett., vol. 18, no. 1,
pp. 47–50, Jan. 2011.
[31] F. A. Tobar and D. P. Mandic, “The quaternion kernel least squares,”
in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP),
May 2013, pp. 6128–6132.
[32] T. Ogunfunmi and T. Paul, “An alternative kernel adaptive ﬁltering
algorithm for quaternion-valued data,” in Proc. Signal Inform. Process.
Assoc. Annu. Summit Conf. (APSIPA), Dec. 2012, pp. 1–5.
[33] N. Jacobson, The Theory of Rings. Providence, RI, USA: AMS, 1943.
[34] N. Jacobson, Basic Algebra I. New York, NY, USA: Dover, 2009.
[35] F. G. Frobenius, “Über lineare substitutionen und bilineare formen,”
J. Reine Angew. Math., vol. 84, pp. 1–63, 1878.
[36] F. Anderson and K. Fuller, Rings and Categories of Modules (Grad-
uate Texts in Mathematics), vol. 13, 2nd ed. New York, NY, USA:
Springer-Verlag, 1992.
[37] W. Adkins and S. Weintraub, Algebra: An Aproach Via Module Theory
(Graduate Texts in Mathematics). New York, NY, USA: Springer-Verlag,
1992.
[38] J. Mercer, “Functions of positive and negative type, and their connection
with the theory of integral equations,” Philosoph. Trans. Roy. Soc.
London A, vol. 209, pp. 415–446, Nov. 1909.
[39] G. Pedrick, Theory of Reproducing Kernels for Hilbert Spaces of Vector
Valued Functions (Studies in Eigenvalue Problems). Lawrence, KS,
USA: Univ. Kansas, 1957.
[40] L.
Schwartz,
“Sous-espaces
Hilbertiens
d’espaces
vectoriels
topologiques et noyaux associés (noyaux reproduisants),” J. d’Anal.
Math., vol. 13, no. 1, pp. 115–256, 1964.
[41] S.-Y. Kung, Kernel Methods and Machine Learning. Cambridge, U.K.:
Cambridge Univ. Press, 2014.
[42] M. Gönen and E. Alpaydın, “Multiple kernel learning algorithms,”
J. Mach. Learn. Res., vol. 12, pp. 2211–2268, Jul. 2011.
[43] M. Yukawa, “Multikernel adaptive ﬁltering,” IEEE Trans. Signal
Process., vol. 60, no. 9, pp. 4672–4682, Sep. 2012.
[44] M. Yukawa, “Nonlinear adaptive ﬁltering techniques with multiple
kernels,” in Proc. Eur. Signal Process. Conf., 2011, pp. 136–140.
[45] J. P. Ward, Quaternions and Cayley Numbers: Algebra and Applications.
Norwell, MA, USA: Kluwer, 1997.
[46] S. J. Sangwine and N. L. Bihan. (2005). Quaternion Toolbox for
MATLAB [Online]. Available: http://qtfm.sourceforge.net/
[47] I. Steinwart, D. Hush, and C. Scovel, “An explicit description of the
reproducing kernel Hilbert spaces of Gaussian RBF kernels,” IEEE
Trans. Inf. Theory, vol. 52, no. 10, pp. 4635–4643, Oct. 2006.
[48] F. A. Tobar, L. Yacher, R. Paredes, and M. E. Orchard, “Anomaly
detection in power generation plants using similarity-based model-
ing and multivariate analysis,” in Proc. Amer. Control Conf. (ACC),
Jun./Jul. 2011, pp. 1940–1945.
[49] C.-J. Lin, S.-J. Hong, and C.-Y. Lee, “Using least squares support vector
machines for adaptive communication channel equalization,” Int. J. Appl.
Sci. Eng., vol. 3, no. 1, pp. 51–59, 2005.
[50] T. A. Ell and S. J. Sangwine, “Quaternion involutions and anti-
involutions,” Comput. Math. Appl., vol. 53, no. 1, pp. 137–143, 2007.
[51] C. C. Took and D. P. Mandic, “A quaternion widely linear adaptive
ﬁlter,” IEEE Trans. Signal Process., vol. 58, no. 8, pp. 4427–4431,
Aug. 2010.
[52] C. Jahanchahi, C. C. Took, and D. P. Mandic, “On HR calculus,
quaternion valued stochastic gradient, and adaptive three dimensional
wind forecasting,” in Proc. Int. Joint Conf. Neural Netw. (IJCNN),
Jul. 2010, pp. 1–5.
[53] S. C. Douglas, “Widely-linear recursive least-squares algorithm for
adaptive beamforming,” in Proc. IEEE Int. Conf. Acoust., Speech Signal
Process., (ICASSP), Apr. 2009, pp. 2041–2044.
[54] D. P. Mandic and S. L. Goh, Complex Valued Nonlinear Adaptive Filters:
Noncircularity, Widely Linear and Neural Models. New York, NY, USA:
Wiley, 2009.
Felipe A. Tobar received the B.Sc. and M.Sc. degrees in Electrical and
Electronic Engineering from Universidad de Chile, Santiago, Chile in 2008
and 2010 respectively. He is currently pursuing his Ph.D. degree in Signal
Processing at Imperial College London, London, U.K.
His research interests lie within the interface between signal processing and
machine learning, and include high-dimensional kernel regression, Bayesian
system identiﬁcation, and nonlinear adaptive ﬁltering.
Danilo P. Mandic is a Professor in signal processing with Imperial College
London, London, U.K., where he has been working in the area of nonlinear
adaptive signal processing and nonlinear dynamics. He has been a Guest
Professor with Katholieke Universiteit Leuven, Leuven, Belgium and a
Frontier Researcher with RIKEN, Tokyo. His publication record includes two
research monographs titled Recurrent Neural Networks for Prediction (West
Sussex, U.K.: Wiley, August 2001) and Complex-Valued Nonlinear Adaptive
Filters: Noncircularity, Widely Linear and Neural Models (West Sussex, U.K.:
Wiley, April 2009), an edited book titled Signal Processing for Information
Fusion (New York: Springer, 2008), and more than 200 publications on signal
and image processing.
He has been a member of the IEEE Technical Committees on Signal
Processing Theory and Methods and Machine Learning for Signal Processing,
an Associate Editor for the IEEE TRANSACTIONS ON CIRCUITS AND
SYSTEMS II, the IEEE TRANSACTIONS ON SIGNAL PROCESSING, the IEEE
TRANSACTIONS ON NEURAL NETWORKS, and the IEEE SIGNAL PROCESS-
ING MAGAZINE. He has produced award winning papers and products from
his collaboration with the industry, and has received President’s Award for
excellence in postgraduate supervision at Imperial College. He is a member
of the London Mathematical Society.
