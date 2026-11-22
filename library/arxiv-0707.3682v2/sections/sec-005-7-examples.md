---
doc_id: arxiv-0707.3682v2
doc_title: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS"
section_id: sec-005-7-examples
section_title: "Examples"
section_number: 7
pages: 30-34
source_pdf: 0707.3682v2.pdf
source_sha256: 609a6f67a0cd5fc8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.963
doc_brief: "ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS — We formulate a conjectural p-adic analogue of Borel’s theorem re- lating regulators for higher K-groups of number ﬁelds to special values of the"
---
[]{#examplesection label="examplesection"}

In this section we describe the evidence for Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"} in the case of primitive idempotents $\pi$ in $E[\Gal(k/\Q)]$ as in Examples [\[S3example\]](#S3example){reference-type="ref" reference="S3example"}, [\[D8example\]](#D8example){reference-type="ref" reference="D8example"} and [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"}, with $E=\Q$ in the first two and $E=\Q(\z_3)$ in the last. In the first two cases part (1) of the conjecture is known by Proposition [\[grossprop\]](#grossprop){reference-type="ref" reference="grossprop"}, but in the last case our evidence for this part is numerical; the same holds for parts (2) through (4) in all cases.

We would like to stress that the numerical verification of part (4) of the conjecture actually proves this part for all cases that we considered since we can check that a element of $E\tensor\Qp$ is a unit of that ring by computing a close enough approximation of it.

For the numerical calculations of the regulator, $R_{n,p}(M_\pi^E)$, we assumed that the syntomic regulator map on the subgroup of $\Kn k$ described in Zagier's Conjecture [\[zagierconjecture\]](#zagierconjecture){reference-type="ref" reference="zagierconjecture"} is given by the $\tLmod n ^\s$ (as in Remark [\[synregremark\]](#synregremark){reference-type="ref" reference="synregremark"}). Out of the many possible choices for $\Lmod n (z)$ as described in  [\[Pnpdef\]](#Pnpdef){reference-type="eqref" reference="Pnpdef"} we used $$\Lmod n (z) = \Li_{n,p}(z) - \log_p^{n-1}(z) \Li_1(z) / n!
            = \Li_{n,p}(z) + \log_p^{n-1}(z) \log_p(1-z) / n!$$ since it is relatively simple from a computational point of view. The calculations of the $\Lmod n (z)$ for the branch with $\log_p(p)=0$ were done in versions 2.11-7, 2.12-19 and 2.12-21 of [@magma], using an implementation of the algorithm described in [@BdJ06].

Note that the primitive idempotents in Examples [\[S3example\]](#S3example){reference-type="ref" reference="S3example"} and [\[D8example\]](#D8example){reference-type="ref" reference="D8example"} are unique up to conjugation in $\Q[G]$ since they all correspond to $\pi_2$. But in Example [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"} replacing $\z_3$ with $\z_3^2$ changes a primitive idempotent corresponding to $\pi_3$ into one corresponding to $\pi_4$, and conversely. Because the same holds for the classical and (with values in $E \tensor_\Q \C$ and $E \tensor_\Q \Qp$ respectively), as well as the Euler factor for $p$, the conjectures for primitive idempotents corresponding to $\pi_3$ and $\pi_4$ are actually equivalent.

In Examples [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"}, [\[D8realcomputation\]](#D8realcomputation){reference-type="ref" reference="D8realcomputation"} and [\[D8CMcomputation\]](#D8CMcomputation){reference-type="ref" reference="D8CMcomputation"} we have $E=\Q$ so that we identify $E\tensor_\Q \C$ with $\C$, etc., and use notation as in Remark [\[idenrem\]](#idenrem){reference-type="ref" reference="idenrem"}.

$$\begin{array}{cc}#1\end{array}$$

=cmcsc9

::: center
Table 1. Splitting field of $x^3
 - x^2
 - 3 x
 + 1$, where $C(\chi_\pi) = 2^{2}\cdot37$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00010101001000000010000101111100100010101110100110010110110011000000)\_2\^0 3 & (1.010012121202211021200001102121121100201201100121200211021212)\_3\^4 5 & (4.2320143330214023104113344110103131003140)\_5\^6 7 & (6.354304301412412415450326016336635)\_7\^6 11 & (2.62161235A928A3423563A7888A)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.00000010100111000100001100100011111010110000101001101110011000101000)\_2\^2 3 & (1.1202122002221002110112100012002001211111011101010220)\_3\^0 5 & (4.11040024440232442233024131040014140)\_5\^0 7 & (5.23516363226501261362543533110)\_7\^0 11 & (A.9542728A692401225487A278)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00001010110110011101000011101001000001100000100010000011011110011101)\_2\^6 3 & (1.200111022020102011202110020222210102001020101122110122022)\_3\^12 5 & (3.214210342400224303122204142313310423002)\_5\^8 7 & (1.2103004405355450123124426604231)\_7\^10 11 & (1.2069AA607609242834655465)\_11\^10 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.00000101111001110001111000010111110100101010001010001001100111100011)\_2\^2 3 & (1.2022122002112102001110211120022002211212022201001210)\_3\^0 5 & (3.34404422113121141420412040113130342)\_5\^0 7 & (4.66001565513622316645262615350)\_7\^0 11 & (1.1A26918431A09200099A81A7)\_11\^0

::: center
Table 2. Splitting field of $x^3
 - 6 x
 - 2$, where $C(\chi_\pi) = 2^{2}\cdot3^{3}\cdot7$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.10000001110000110101010101111101011001000101111010100001000101111010)\_2\^0 3 & (2.1122020011220001210112202100011222122000102121211020022012)\_3\^4 5 & (3.4232302100220101433222440213432224202143)\_5\^6 7 & (4.2544363600510010013523314315122)\_7\^7 11 & (5.481569541633A6875525A00911)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01111101110011001100110111100111100010100000100110111100101110110010)\_2\^2 3 & (1.1211000101210110112021221022022211101101102021011220)\_3\^0 5 & (2.13000020122302011221412322140400441)\_5\^0 7 & (4.55510152416245405156545556000)\_7\^2 11 & (1.14A21577033A19227344806A)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.10101101100000101100101100100110101101111111000110011100110000011111)\_2\^6 3 & (2.120122222011210012110212011212210211022212221020022201)\_3\^14 5 & (4.040210142044334334412003042243311012202)\_5\^8 7 & (3.2403415331415026502116243110353)\_7\^9 11 & (7.160964096503643537518492)\_11\^10 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01010111000010111011111101010101111011001011010111110100101100010111)\_2\^2 3 & (1.2002000121100001212101001020022211022201122100111000)\_3\^0 5 & (4.44311102333442121212402410333144343)\_5\^0 7 & (3.41526030363465662002262442000)\_7\^0 11 & (2.687349321A27130485753530)\_11\^0

::: center
Table 3. Splitting field of $x^3
 - 4 x
 - 1$, where $C(\chi_\pi) = 229$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01110100101010000001111100101001000110110101000001001011100111100010)\_2\^0 3 & (2.012012211010121011021101220021012212100110002220200211021221)\_3\^4 5 & (4.3433241433301132322003123241441021322342)\_5\^6 7 & (6.262401634562505353633061004510116)\_7\^6 11 & (3.6717A20401481085265342054)\_11\^7 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01100001011001101110100010111011001000000110000010000100110111111101)\_2\^3 3 & (2.2120211202111122100220011211121110002020101200021220)\_3\^0 5 & (3.03414332241433441404241012442104412)\_5\^0 7 & (3.24033044132523034433054506150)\_7\^0 11 & (9.21A61A480A10801760893710)\_11\^1 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11110110101010011011010001011100111001101011001101110111000000010001)\_2\^5 3 & (2.222112021012010001201220011021022211112022112001020100)\_3\^16 5 & (4.3414223144333221124000410221113420102)\_5\^10 7 & (2.5612036605646266635264251053110)\_7\^10 11 & (8.5A9220278400758A0193AA6)\_11\^11 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01010000111010100010011010011100110010001101000101101100101100100011)\_2\^3 3 & (2.1121000022222000210222202101202022011021200021010220)\_3\^0 5 & (4.42011132342110332341130324344440134)\_5\^0 7 & (1.25032245164656402236525435500)\_7\^0 11 & (5.375705346AA0810959728302)\_11\^0

::: center
Table 4. Splitting field of $x^3
 - 6 x^2
 + 2$, where $C(\chi_\pi) = 2^{2}\cdot3^{4}\cdot5$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11110010110000001011011110010111010011100101111011011000111111110001)\_2\^0 3 & (2.120020100000012102010221000201210120200202222221111002100)\_3\^6 5 & (3.3432222440014423344440441124111231400414)\_5\^4 7 & (5.611651266622656555064166304513241)\_7\^6 11 & (2.805A8344265760A69A2490828A)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10100000100110111110111110101101001001110101011111100111101100001111)\_2\^2 3 & (1.1120211121012011012202202010100211210110122222201210)\_3\^0 5 & (2.13242313233011201133333143412022134)\_5\^0 7 & (3.00123442142613541412624063510)\_7\^0 11 & (2.2725A17844929880A8412281)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00010100011011001110000011110010000100001101100111101000101001001110)\_2\^7 3 & (1.0200220011011111211112101212120212201200221122102001)\_3\^18 5 & (1.321100221113142104412032003401031323110)\_5\^7 7 & (3.5553063665305405650105042513546)\_7\^10 11 & (A.568607725325302A5663A746)\_11\^10 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10111101010011001111001000001111111000110110101100010100000000001010)\_2\^2 3 & (1.0002101112212121121001002201100122111211210111102110)\_3\^0 5 & (2.30334130213120322410240113023441000)\_5\^0 7 & (4.62042101122332630656130062420)\_7\^0 11 & (5.491153185997A48326862A46)\_11\^0

::: center
Table 5. Splitting field of $x^4
 - x^3
 - 3 x^2
 + x
 + 1$, where $C(\chi_\pi) = 5\cdot29$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11111010111100011100011000110000111000001111111101101000111001001001)\_2\^2 3 & (1.201220211120010110010200120221012101101121011201212202210212)\_3\^5 5 & (2.21221421224100432231134432324224211113143)\_5\^3 7 & (2.260524146626624605001621634435032)\_7\^6 11 & (2.74697855444977862531A25026)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01010010100111000101001000111001101011100000001100110101111010001100)\_2\^2 3 & (1.1011210202202201201020222100121100002100020220220021)\_3\^0 5 & (4.30210324423422014142420103340302330)\_5\^0 7 & (1.16355063143251352506540201034)\_7\^0 11 & (9.9A7720A981020A9A32071790)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01101101001101100011000000000011101110110010001010001100111111101001)\_2\^8 3 & (1.0002011102111201211120012012011221112210212111112002202122)\_3\^12 5 & (1.030204001130134123130241412102302410321)\_5\^7 7 & (5.6213331545344431613600254300115)\_7\^10 11 & (9.98414459608789A37989AA86)\_11\^10 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01111100101100101110101001110010110011011010001011101111000000111001)\_2\^2 3 & (1.1111012010001010110000200000021011010010220212100211)\_3\^0 5 & (4.01341421411140002024312030010110013)\_5\^0 7 & (4.10032134632553222245313526015)\_7\^0 11 & (8.6637671480756A9916284377)\_11\^0

::: center
Table 6. Splitting field of $x^4
 - 2 x^3
 - 3 x^2
 + 4 x
 + 1$, where $C(\chi_\pi) = 2^{2}\cdot3^{2}\cdot11$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11001111111100110011011000011011110100000010001100010000111000001110)\_2\^5 3 & (1.101222112200111120002122200210022002021121200101112022212121)\_3\^2 5 & (1.3213042203212141302102134014142431100344)\_5\^6 7 & (1.444434205533111532005253505615656)\_7\^6 11 & (9.61613555149153993505670160)\_11\^5 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.11110101101001001100111001001100001010010111011100011010101000010001)\_2\^4 3 & (1.1221211120021010011021120022021022220202012220120020)\_3\^0 5 & (1.03123432421241311210024333243134200)\_5\^0 7 & (1.20515104501535164355503412253)\_7\^0 11 & (4.A19905A97667183A61256312)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.10101000100011001001110000000110011010000011010001100100101100100011)\_2\^16 3 & (2.00020011020011210121200021121000100102202022102012021120)\_3\^10 5 & (3.043124340101142041302443131432222411101)\_5\^8 7 & (3.1016042121151553442503432550426)\_7\^10 11 & (4.A244AA713986547114383)\_11\^13 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01011001111000100100100110110111001110010101101110101100000001001101)\_2\^4 3 & (1.2200111010220200001122120000000211211201112212022102)\_3\^0 5 & (4.31111224412403210010123414333414223)\_5\^0 7 & (2.63463651641424006321031014001)\_7\^0 11 & (2.054143779893294A023A2760)\_11\^1

::: center
Table 7. Splitting field of $x^4
 - 6 x^2
 + 6$, where $C(\chi_\pi) = 2^{7}\cdot3^{2}$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11111110110101110110001001001000100111010011011111000101011110110110)\_2\^10 3 & (2.022112012020121000012010222021210101120000211220112222110100)\_3\^2 5 & (2.041234240331110012313440303434111221114)\_5\^7 7 & (4.126126412601443066506634321456330)\_7\^6 11 & (1.508753A40028580A83265A6397)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.00111001111010100110000110000111111000001101110001010000100110100110)\_2\^2 3 & (1.1102020120122110111012211100112220010211120222001022)\_3\^0 5 & (3.24102423421030322330312322041041320)\_5\^1 7 & (3.53421553111552403452502135351)\_7\^0 11 & (9.993168A73395501045A926A6)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01000011110101000111110110010101100000101100100001110011010100110111)\_2\^27 3 & (1.20110210022121202120201021000120210110011111202222221202)\_3\^10 5 & (4.13321010222213321143100244321412404344)\_5\^9 7 & (1.6542260045104311315015635541014)\_7\^10 11 & (4.35786968692892127976707)\_11\^11 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.00100100101111111001101001011101011111110110100110100000111111010001)\_2\^2 3 & (1.0101222010121001211100001210022220120122121200102122)\_3\^0 5 & (2.44334240213144033340330341233100231)\_5\^0 7 & (2.43613231343555620664002413300)\_7\^0 11 & (A.957125591551731675713855)\_11\^0

::: center
Table 8. Splitting field of $x^4
 - 6 x^2
 - 4 x
 + 2$, where $C(\chi_\pi) = 2^{5}\cdot17$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.10111000110111011100110001011111110001011110100001100011100001101001)\_2\^7 3 & (1.1001122110011102222210022111010102000101002122001210120111212)\_3\^4 5 & (2.1330133431400143111041343243044132341000)\_5\^6 7 & (1.251366021640656215554304534633666)\_7\^6 11 & (6.8781153571182A7A3A52578590)\_11\^6 to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01100101000011011110000111011100100110110110111011000100000101100110)\_2\^5 3 & (2.2111111121010122120102220010120102202210101102021112)\_3\^0 5 & (2.03010131243321342244201240202313243)\_5\^0 7 & (2.45653546525345623002012601006)\_7\^0 11 & (1.5054539309942A8686113521)\_11\^0 to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01101001100111100011100000011101100011011111111011011010000000100111)\_2\^19 3 & (1.0022021200111200200110022100110101220100021201020020021001)\_3\^12 5 & (4.41122221322441142131444023001440141102)\_5\^9 7 & (4.6425656621000232634542266362653)\_7\^10 11 & (5.30669526A542413A15559106)\_11\^10 to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10000111001100100001010000010001000011100111101011000000110111100101)\_2\^5 3 & (2.1100001122200222122120000002011201000121010120122102)\_3\^0 5 & (1.00313434131411434403030110103232430)\_5\^1 7 & (4.51404541504052312152404613255)\_7\^0 11 & (2.A43315061300727A39739622)\_11\^0

::: center
Table 9. Splitting field of $x^4
 - 2 x^3
 + 5 x^2
 - 4 x
 + 2$, where $C(\chi_\pi) = 2^{3}\cdot17$.
:::

to 10 pt $p$&to 330 pt$R_{2,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11110000011111000100011010100111010001000101111111000010111001000001)\_2\^8 3 & (1.2001010102220112101111101220000000012020211022222012112010122)\_3\^4 5 & (2.01203020434342403202140220421203111323421)\_5\^4 7 & (4.1140305454665411023106103225364300)\_7\^4 11 & (9.074667649A54466861880828A41)\_11\^4 to 10 pt $p$&to 330 pt$\Lp p {2} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<2\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10011100010001001110011010011101110110111100101101100011101101010011)\_2\^6 3 & (1.2211021011200210000101010021221011201210202220121211)\_3\^0 5 & (4.33003403101112402103034043124123020)\_5\^0 7 & (6.55655254400302602216266140200)\_7\^0 11 & (4.84968AAA0466783629843316)\_11\^0 to 10 pt $p$&to 330 pt$R_{4,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01111010101011110100100110010011000001110001101011101000010011010010)\_2\^15 3 & (2.02020202222222212011121000222200020002221002201220201002211)\_3\^10 5 & (3.121141434441031100040041101320123332342)\_5\^8 7 & (4.30103246365105165401451263010636)\_7\^8 11 & (9.8864321414815928A83132426)\_11\^8 to 10 pt $p$&to 330 pt$\Lp p {4} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<4\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10101000111010101100110000110001001011001001001001010011001010011101)\_2\^7 3 & (1.0220110000101201002201220101112220112012211122211111)\_3\^0 5 & (4.24124003322330023340322023204112410)\_5\^0 7 & (1.34631136124161206563156313232)\_7\^0 11 & (6.484018160860423737043861)\_11\^0

::: center
Table 10. Splitting field of $x^4
 - x^3
 + 3 x^2
 - 2 x
 + 4$, where $C(\chi_\pi) = 5\cdot41$.
:::

to 10 pt $p$&to 330 pt$R_{2,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00100101101010001111110110001011010111110011100101011001110011011000)\_2\^6 3 & (2.0021220111220210202122211101102111121010022202210012111112202)\_3\^4 5 & (4.2413230212134320403404223440242144143010)\_5\^4 7 & (5.6622665100264660251241453165220553)\_7\^4 11 & (2.0A380682536A50856633A5963AA)\_11\^4 to 10 pt $p$&to 330 pt$\Lp p {2} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<2\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10001100100010010110110100011001000110001101100111111011111110000000)\_2\^5 3 & (1.0000112110000221101100101100220112122121100200111220)\_3\^0 5 & (3.31322324200110323444242424141204000)\_5\^1 7 & (6.20642211231410105634103112315)\_7\^0 11 & (4.8488929AA248277415458863)\_11\^0 to 10 pt $p$&to 330 pt$R_{4,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01101011011011001001110001011011001001100001000100001111001011100010)\_2\^9 3 & (2.12201221002111122111110002102122122100002111212000210102220)\_3\^10 5 & (3.03433213241214232102131324212010224400)\_5\^8 7 & (3.21341424531605465104510422214051)\_7\^8 11 & (A.180567AA0545A59652909A250)\_11\^8 to 10 pt $p$&to 330 pt$\Lp p {4} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<4\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.11100001111100101110011000101000001100001100100001000011000001000111)\_2\^6 3 & (1.2110210100202111000001112120121020120200000202111102)\_3\^0 5 & (1.22414201312142130131112334430123200)\_5\^1 7 & (6.66200605216643655434600606423)\_7\^0 11 & (3.5059939560A2AA91106844A7)\_11\^0

::: center
Table 11. Splitting field of $x^4
 - 2 x^3
 + 6 x^2
 - 5 x
 + 2$, where $C(\chi_\pi) = 13\cdot17$.
:::

to 10 pt $p$&to 330 pt$R_{2,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.11100111011011110110000110110011010010001100010000011011000000100011)\_2\^7 3 & (1.001110110101022221010202101001220021110111221112100200010011)\_3\^5 5 & (4.12002342224442011223100142021013114003331)\_5\^4 7 & (6.0065051533250322312551556340446112)\_7\^4 11 & (9.58602382412A681650341722097)\_11\^4 to 10 pt $p$&to 330 pt$\Lp p {2} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<2\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.01010001000000000001000000101011111111001100001000001100111111100100)\_2\^6 3 & (2.0212122200002021202200211122100200001001012201202000)\_3\^1 5 & (2.12300004023110442141103112001044200)\_5\^0 7 & (5.65035644055466446205106662353)\_7\^0 11 & (6.38803A213738A731776470A4)\_11\^0 to 10 pt $p$&to 330 pt$R_{4,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.01010110010100100110100011110011010001011010001010001001110111101010)\_2\^10 3 & (1.1111010110110112222112002001211122102011200022210022220110)\_3\^11 5 & (2.300041000440134413002331411231121430312)\_5\^8 7 & (2.63246241360463115315231424221502)\_7\^8 11 & (A.49299953329A1125214A939A7)\_11\^8 to 10 pt $p$&to 330 pt$\Lp p {4} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<4\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.00100111010100001110011000011111110110110001001100110010111000011110)\_2\^7 3 & (1.2001110201210120022112022021221001220010010202222220)\_3\^1 5 & (4.31111034231223303224440300102101300)\_5\^0 7 & (3.23250645010664211233114156026)\_7\^0 11 & (6.722A82921527466612856704)\_11\^0

::: center
Table 12. Splitting field of $x^4
 + 3 x^2
 - 6 x
 + 6$, where $C(\chi_\pi) = 2^{2}\cdot3^{2}\cdot11$.
:::

to 10 pt $p$&to 330 pt$R_{2,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00011111110011010111101100110001100000010001000010010011001000110100)\_2\^6 3 & (2.001121000222211121002102201101101100211202000001120001201101)\_3\^2 5 & (4.32211042044110431112434230011130322040334)\_5\^4 7 & (6.460003406606016165433631101363300)\_7\^5 11 & (4.355421A54525023347874A49229)\_11\^3 to 10 pt $p$&to 330 pt$\Lp p {2} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<2\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.11101000100101000011100111111110011101011000001101111010111100101100)\_2\^5 3 & (1.2022010222110011100120101011011011020010020011221012)\_3\^0 5 & (3.22012020201133014223242323022213400)\_5\^0 7 & (2.43314511556206561022451602200)\_7\^1 11 & (7.514814537963976728A46001)\_11\^0 to 10 pt $p$&to 330 pt$R_{4,p}(M_\pi)/D(M_\pi)^{1/2,p}$ 2 & (1.00011101001000000111110111000101001111110011011101001101001001110101)\_2\^11 3 & (2.0222010120001012000101112011222120000210000112021000101001)\_3\^8 5 & (4.200024100322411004323111441041141020122)\_5\^8 7 & (5.12536440256103300364331512021150)\_7\^8 11 & (6.6966231827671A91984A434A7)\_11\^7 to 10 pt $p$&to 330 pt$\Lp p {4} {\chi_\pi\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<4\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & (1.10111000101101010100110110100100101011000111100000010010100110001101)\_2\^6 3 & (1.0221110122220100011212020012222021100000010022110011)\_3\^0 5 & (3.44200104443132341021214030231112200)\_5\^0 7 & (4.44003540500226200364534021346)\_7\^0 11 & (5.766584290652809A28501199)\_11\^0

::: center
Table 13. Splitting field of $x^6
 - x^5
 - 6 x^4
 + 7 x^3
 + 4 x^2
 - 5 x
 + 1$, where $C(\chi_\pi\tensor\id) = 2^{2}\cdot5\cdot19$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.010101011100101010)\_2\^4) + \_3 ((1.111100111000011101)\_2\^2) 3 & 1((2.121122121210110121)\_3\^4) + \_3 ((1.100202121120121202)\_3\^4) 5 & 1((4.402020001241122012)\_5\^3) + \_3 ((1.402102204113114001)\_5\^4) 7 & 1((2.1404154326422162)\_7\^6) + \_3 ((5.1444362630564332)\_7\^6) 11 & 1((6.9026829596822)\_11\^6) + \_3 ((8.048680429402A)\_11\^6) to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.010111010101101000)\_2\^4) + \_3 ((1.111111110001001011)\_2\^2) 3 & 1((1.120012101022112222)\_3\^0) + \_3 ((2.212202101110022110)\_3\^0) 5 & 1((1.222321004420021231)\_5\^0) + \_3 ((1.123432442320044212)\_5\^0) 7 & 1((6.215644553551135401)\_7\^0) + \_3 ((1.642236344041330514)\_7\^0) 11 & 1((6.6A0036761338492361)\_11\^0) + \_3 ((8.749011AA3694540145)\_11\^0) to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.000011100001001101)\_2\^9) + \_3 ((1.101010111001110110)\_2\^9) 3 & 1((1.110110120010021222)\_3\^12) + \_3 ((2.020220021122220210)\_3\^12) 5 & 1((3.020013014242432200)\_5\^7) + \_3 ((1.220134043203242432)\_5\^7) 7 & 1((4.15141551064450)\_7\^10) + \_3 ((6.53120060244502)\_7\^10) 11 & 1((4.285500134)\_11\^12) + \_3 ((2.A3934821906)\_11\^10) to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.110010010001000101)\_2\^4) + \_3 ((1.111111100101010110)\_2\^2) 3 & 1((1.211021010101222221)\_3\^0) + \_3 ((2.122212200211101011)\_3\^0) 5 & 1((1.401222401123304240)\_5\^0) + \_3 ((1.432224122043203014)\_5\^0) 7 & 1((2.441442356342000541)\_7\^0) + \_3 ((3.664531413660053644)\_7\^0) 11 & 1((6.3A4A10A60052302518)\_11\^0) + \_3 ((4.7AA8843572652457A4)\_11\^0)

::: center
Table 14. Splitting field of $x^6
 - x^5
 - 8 x^4
 - x^3
 + 12 x^2
 + 7 x
 + 1$, where $C(\chi_\pi\tensor\id) = 2^{2}\cdot5\cdot31$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.100100010111101000)\_2\^2) + \_3 ((1.111010100101111010)\_2\^0) 3 & 1((1.221220200011201020)\_3\^4) + \_3 ((2.020111011200022220)\_3\^4) 5 & 1((1.141130342002111122)\_5\^3) + \_3 ((4.342032011212400441)\_5\^3) 7 & 1((4.4505556355566640)\_7\^6) + \_3 ((3.0610023664215014)\_7\^6) 11 & 1((7.3700473650A19)\_11\^6) + \_3 ((1.3659A52396880)\_11\^6) to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.101110001100101000)\_2\^2) + \_3 ((1.010100111010111101)\_2\^4) 3 & 1((2.111112222201000112)\_3\^0) + \_3 ((1.120112022212020122)\_3\^0) 5 & 1((4.321142113321234330)\_5\^0) + \_3 ((1.130134403242024422)\_5\^0) 7 & 1((5.530006300632330553)\_7\^0) + \_3 ((2.200601212403230506)\_7\^0) 11 & 1((2.00762927347972431A)\_11\^0) + \_3 ((A.191A1780051997A650)\_11\^0) to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.011100011000010010)\_2\^8) + \_3 ((1.011100000000101011)\_2\^8) 3 & 1((2.202202022111202222)\_3\^14) + \_3 ((1.112002110200111001)\_3\^15) 5 & 1((3.141433024141141322)\_5\^8) + \_3 ((2.002014030014311244)\_5\^7) 7 & 1((6.50135302661002)\_7\^10) + \_3 ((4.04356114536113)\_7\^10) 11 & 1((5.A3306A68921)\_11\^10) + \_3 ((3.85A6650344A)\_11\^10) to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.100110110011011000)\_2\^2) + \_3 ((1.110110100001011101)\_2\^4) 3 & 1((2.201101211210020202)\_3\^0) + \_3 ((1.212021202011010201)\_3\^0) 5 & 1((4.011013012410044000)\_5\^0) + \_3 ((1.431333301302323324)\_5\^0) 7 & 1((2.130552365243450401)\_7\^0) + \_3 ((2.601221155363314062)\_7\^0) 11 & 1((9.53274A487A14818064)\_11\^0) + \_3 ((9.89A625650825167861)\_11\^0)

::: center
Table 15. Splitting field of $x^6
 - x^5
 - 8 x^4
 + 5 x^3
 + 19 x^2
 - 4 x
 - 11$, where $C(\chi_\pi\tensor\id) = 5\cdot139$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.000110100111100100)\_2\^4) + \_3 ((1.000011011101110010)\_2\^5) 3 & 1((2.102212010212021001)\_3\^4) + \_3 ((2.122111112211000220)\_3\^4) 5 & 1((1.400211310114320013)\_5\^3) + \_3 ((1.434230430334022423)\_5\^3) 7 & 1((2.2523154003106061)\_7\^6) + \_3 ((2.3200021260361110)\_7\^6) 11 & 1((9.4472801A61A44)\_11\^6) + \_3 ((1.7232221727046)\_11\^6) to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.000100101010000101)\_2\^4) + \_3 ((1.000010100000000110)\_2\^3) 3 & 1((2.111012101221111220)\_3\^2) + \_3 ((1.010011111201220212)\_3\^0) 5 & 1((3.240243311024013404)\_5\^0) + \_3 ((4.142342004244233331)\_5\^2) 7 & 1((6.543343430631523116)\_7\^1) + \_3 ((2.342260265363120032)\_7\^0) 11 & 1((4.8521241A647A883282)\_11\^0) + \_3 ((1.46220220356163464A)\_11\^0) to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.000100111100110101)\_2\^10) + \_3 ((1.011111001011110010)\_2\^9) 3 & 1((1.202001002112012221)\_3\^13) + \_3 ((1.021221211222021020)\_3\^12) 5 & 1((3.404332041431011004)\_5\^7) + \_3 ((3.213210304101144004)\_5\^7) 7 & 1((4.11031052300040)\_7\^10) + \_3 ((4.03411453000015)\_7\^10) 11 & 1((6.8523188534)\_11\^11) + \_3 ((5.2A39A447198)\_11\^10) to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.101001011001000000)\_2\^4) + \_3 ((1.000100011110101010)\_2\^3) 3 & 1((1.200212010102010102)\_3\^1) + \_3 ((1.122011112111021002)\_3\^0) 5 & 1((3.124113213204101323)\_5\^0) + \_3 ((2.114244212313224030)\_5\^3) 7 & 1((6.430024313466045624)\_7\^0) + \_3 ((5.065261416212661354)\_7\^0) 11 & 1((5.A88931A0106A0172A3)\_11\^0) + \_3 ((3.A4151A485571789978)\_11\^0)

::: center
Table 16. Splitting field of $x^6
 - x^5
 - 8 x^4
 + 11 x^3
 + 2 x^2
 - 5 x
 + 1$, where $C(\chi_\pi\tensor\id) = 2^{2}\cdot3^{2}\cdot13$.
:::

to 10 pt $p$&to 330 pt$R_{3,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.101100110101111100)\_2\^2) + \_3 ((1.001000001010110111)\_2\^0) 3 & 1((2.021221201100120120)\_3\^5) + \_3 ((2.020012210111121212)\_3\^7) 5 & 1((3.000431031211204434)\_5\^6) + \_3 ((1.012314421212444244)\_5\^6) 7 & 1((3.0426445363200511)\_7\^6) + \_3 ((1.1035504615611621)\_7\^6) 11 & 1((8.9799A36158285)\_11\^6) + \_3 ((9.229923AAA0734)\_11\^6) to 10 pt $p$&to 330 pt$\Lp p {3} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<3\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.100100111001100011)\_2\^2) + \_3 ((1.101001000011101110)\_2\^4) 3 & 1((1.022110110201121122)\_3\^2) + \_3 ((2.102110200120211001)\_3\^0) 5 & 1((2.424401443414003124)\_5\^0) + \_3 ((4.440233034214103134)\_5\^0) 7 & 1((5.421026022055251515)\_7\^0) + \_3 ((4.510213122044500212)\_7\^0) 11 & 1((A.187435006878255608)\_11\^0) + \_3 ((6.47020389393AA07A54)\_11\^0) to 10 pt $p$&to 330 pt$R_{5,p}(M_\pi^E)/D(M_\pi^E)^{1/2,p}$ 2 & 1((1.001111100010111111)\_2\^7) + \_3 ((1.100110001101001011)\_2\^8) 3 & 1((1.100222220001012001)\_3\^15) + \_3 ((1.201100102012122102)\_3\^15) 5 & 1((1.302021433120040233)\_5\^8) + \_3 ((1.414010322010320220)\_5\^8) 7 & 1((6.54022035336014)\_7\^10) + \_3 ((1.31434160250212)\_7\^10) 11 & 1((9.5A062420171)\_11\^10) + \_3 ((A.873665790A8)\_11\^10) to 10 pt $p$&to 330 pt$\Lp p {5} {\chi_\pi\hskip-1pt\tensor\omega_p^{\ncount=0\loop\advance\ncount by 1\ifnum\ncount<5\repeat\advance\ncount by -2 -\number\ncount}} {\Q}$ 2 & 1((1.101111101101011100)\_2\^2) + \_3 ((1.001110000011000011)\_2\^4) 3 & 1((2.001012111110022002)\_3\^1) + \_3 ((2.011221210002201001)\_3\^0) 5 & 1((3.241120123211444141)\_5\^1) + \_3 ((2.103430110032401010)\_5\^0) 7 & 1((5.454116060262152231)\_7\^0) + \_3 ((5.160242506230053303)\_7\^0) 11 & 1((9.9950088486A6479846)\_11\^0) + \_3 ((A.178492061888054088)\_11\^0)

::: example
[]{#S3computation label="S3computation"} Let $k$ be a totally real $S_3$-extension of $\Q$. Use notation as in Case 1 of Example [\[S3example\]](#S3example){reference-type="ref" reference="S3example"}, and let $\pi$ be the primitive idempotent corresponding to $\pi_2$ of that example. Since $E=\Q$ we shall write $M_\pi$ instead of $M_\pi^E$ in all notation referring to Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}.

Since $\pi \Kn k = \pi_2 \Kn c$ by Remark [\[galoisdescent\]](#galoisdescent){reference-type="ref" reference="galoisdescent"} we computed the $K$-theory of $c$ using the (numerical) methods of Section [\[practical\]](#practical){reference-type="ref" reference="practical"} and tried to recognize the number $$\label{enM}
e(n,M_\pi)= \L n {\chi_\pi} {\Q} \cdot D(M_\pi)^{1/2,\infty} / R_{n,\infty}(M_\pi)$$ for $n = 3$ and 5 as an element of $\Q^*$ by employing the same methods as described in Section [\[practical\]](#practical){reference-type="ref" reference="practical"} for number fields, where $\L n {\chi_\pi} {\Q}$ was computed as $\z_c(n)/\z_\Q(n)$ (see Example [\[S3L\]](#S3L){reference-type="ref" reference="S3L"}) using Pari-GP [@PARI2]. We succeeded in all cases, and then verified numerically for $p=2$, 3, 5, 7 and 11 if $\Lp p n {\chi_\pi\omega_p^{1-n}} {\Q} \ne 0$ and $$\label{quotientexp}
e(n,M_\pi) \cdot \Eul_p(n, \chi_\pi, \Q) \cdot \dfrac{R_{n,p}(M_\pi)}{D(M_\pi)^{1/2,p}} 
\cdot \Lp p n {\chi_\pi\omega_p^{1-n}} {\Q} ^{-1}$$ in $\Q_p^*$ was equal to 1.

We put our results for the four totally real $S_3$-extensions $k$ of $\Q$ with smallest discriminants in Tables 1 through 4. Note that by Lemma [\[Qpquot\]](#Qpquot){reference-type="ref" reference="Qpquot"} $R_{n,p}(M_\pi) / D(M_\pi)^{1/2,p}$ is in $\Q_p$ and the same holds for $\Lp p n {\chi_\pi\omega_p^{1-n}} {\Q}$ by Lemma [\[pLvalueslemma\]](#pLvalueslemma){reference-type="ref" reference="pLvalueslemma"}, so that (approximations of) those numbers can be easily represented in our tables. We have denoted an element $(a_0+a_1p+a_2p^2+\cdots) \times p^s$ in $\Q_p^*$ with all $a_j$ in $\{0,\dots,p-1\}$ and $a_0\ne0$ by $(a_0.a_1a_2\cdots)_p \times p^s$, writing $A$ to represent 10 when $p = 11$.

For the regulators we computed each $\Lmod n (z)$ up to $O(p^{L(p)})$ with $p^{L(p)}$ approximately equal to $10^{30}$. The relevant part of $R_{n,p}(M_\pi)/D(M_\pi)^{1/2,p}$ has been given in the tables whenever it fitted. For the values of the we can only prove that the relative error is at most $1+O(p^{M(p)})$, where $M(2) = 72$, $M(3) = 47$, $M(5) = 32$, $M(7) = 26$ and $M(11) = 22$. This proves that $\Lp p n {\chi_\pi\omega_p^{1-n}} {\Q}$ does not vanish; together with the verification that [\[enM\]](#enM){reference-type="eqref" reference="enM"} equals 1 numerically this proves part (4) of Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}. The value that we found for [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} was $1+O(p^{N(p)})$ with $N(2) \ge 82$, $N(3) \ge 52$, $N(5) \ge 36$, $N(7) \ge 27$ and $N(11) \ge 24$, giving numerical evidence for parts (2) and (3) of the conjecture, but also suggesting that the relative precision of the value of the is slightly higher than we can prove, justifying the higher precision given in the tables.

Similar calculations were carried out for the next four such $S_3$ extensions and the same primes, with very similar results.
:::

The other examples proceed mostly along the same lines as Example [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"}. The values of $\L n {\chi_\pi} {\Q}$ in Examples [\[D8realcomputation\]](#D8realcomputation){reference-type="ref" reference="D8realcomputation"} and  [\[D8CMcomputation\]](#D8CMcomputation){reference-type="ref" reference="D8CMcomputation"} below were computed using the formula at the end of Example [\[D8L\]](#D8L){reference-type="ref" reference="D8L"}, but in Example [\[sexticcomputation\]](#sexticcomputation){reference-type="ref" reference="sexticcomputation"} the values of $\L n \chi_\pi^E {\Q}$, with $E = \Q(\z_3)$ for $\z_3$ a primitive cube root of unity, were computed using the algorithms described in [@Dok1] and its associated program. In Examples [\[D8realcomputation\]](#D8realcomputation){reference-type="ref" reference="D8realcomputation"} and [\[D8CMcomputation\]](#D8CMcomputation){reference-type="ref" reference="D8CMcomputation"} we determined if $e(n,\chi_\pi)$ (as in [\[enM\]](#enM){reference-type="eqref" reference="enM"}) was in $\Q^*$ using the methods of Section [\[practical\]](#practical){reference-type="ref" reference="practical"}, and for Example [\[sexticcomputation\]](#sexticcomputation){reference-type="ref" reference="sexticcomputation"} we wrote $e(n,M_\pi^E)^{-1} = 1 \tensor a + \z_3 \tensor b$ in $E \tensor_\Q \R$ and then recognized $a$ and $b$ as integers divided by products of some relatively small primes. In each case we then verified for $p=2,\dots,11$ if [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} (or its equivalent) was equal to 1 in $\Qp$ or, for Example [\[sexticcomputation\]](#sexticcomputation){reference-type="ref" reference="sexticcomputation"}, in $\Qp(\z_3)\tensor_\Q\Q = \Qp(\z_3)$. The precision for $\Lmod n (z)$ and the in Examples [\[D8realcomputation\]](#D8realcomputation){reference-type="ref" reference="D8realcomputation"} and [\[D8CMcomputation\]](#D8CMcomputation){reference-type="ref" reference="D8CMcomputation"} was as in Example [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"}. In Example [\[sexticcomputation\]](#sexticcomputation){reference-type="ref" reference="sexticcomputation"} all $\Lmod n (z)$ were computed up to $O(p^{L(p)})$ with $p^{L(p)}$ approximately $10^{16}$ since in this case the check if the equivalent of  [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} is 1 is done in $\Q(\z_3) \tensor_\Q \Qp$ so two coefficients are checked; the values of the in this case, also in $\Q(\z_3)\tensor_\Q \Qp$, were determined up to multiplication by $1\tensor(1+O(p^{M(p)}))$ with $M(p)$ as in Example [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"}.

::: example
[]{#D8realcomputation label="D8realcomputation"} Let $k$ be a totally real $D_8$-extension of $\Q$ as in Case 1 of Example [\[D8example\]](#D8example){reference-type="ref" reference="D8example"}, and use notation as in that example. We again write $M_\pi$ instead of $M_\pi^E$ since $E=\Q$ and consider odd $n \ge 2$. Because $\pi \Kn k = \pi_2 \Kn k_1$ we computed $\Kn k_1$ numerically using the methods of Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"}. Our results with $n=3$ and 5 for the first four such extensions when ordered according to the discriminant are in Tables 5 through 8. The value that we found for [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} in this case was $1+O(p^{N(p)})$ where $N(2) \ge 76$, $N(3) \ge 52$, $N(5) \ge 34$, $N(7) \ge 29$ and $N(11) \ge 22$. Such calculations were also carried out for the next four such extensions, with similar results.
:::

::: example
[]{#D8CMcomputation label="D8CMcomputation"} Let $k$ be a CM Galois extension of $\Q$ with $\Gal(k/\Q) \iso D_8$ as in Case 2 of Example [\[D8example\]](#D8example){reference-type="ref" reference="D8example"}, and use notation as in that example. We again write $M_\pi$ instead of $M_\pi^E$ since $E=\Q$, and consider even $n \ge 2$. Again $\pi \Kn k = \pi_2 \Kn k_1$, so we computed $\Kn k_1$ numerically using the methods of Section [\[ksection\]](#ksection){reference-type="ref" reference="ksection"}. We put our results at $n=2$ and 4 for the first four such extensions when ordered by the value of the (positive) discriminant in Tables 9 through 12. The value that we found for [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} in this case was $1+O(p^{N(p)})$ where $N(2) \ge 79$, $N(3) \ge 53$, $N(5) \ge 35$, $N(7) \ge 27$ and $N(11) \ge 25$. Such calculations were also carried out for the next four such extensions, with similar results.
:::

::: example
[]{#sexticcomputation label="sexticcomputation"} Let $k$ be a totally real $S_3 \times \Z/3\Z$ extension of $\Q$, as in Case 1 of Example [\[sexticexample\]](#sexticexample){reference-type="ref" reference="sexticexample"}. We use notation as in that example, taking $E=\Q(\z_3)$ for a primitive cubic root of unity $\z_3$. A different identification of $\Gal(k/\Q)$ with $S_3 \times \Z/3\Z$ might interchange $\pi_3$ and $\pi_4$ as well as corresponding primitive idempotents, but, as we noted before, the validity of the conjecture for either is equivalent.

Since $\pi \KnE k = \pi_3 \KnE s_1$ we computed $\Kn s_1$ as before. Also, in order to speed up the calculations of the regulator we note that the action of $(e,1)$ and $(\s^2,0)$ on $s_1 = k^{\langle (\s,1) \rangle }$ is the same, so that $\pi = \pi_3 \pi_{H_1}$ and $$(1-\pi_1) ((e,0) + \z_3 (\s,0) + \z_3^2 (\s^2,0))/3 
=
((e,0) + \z_3 (\s,0) + \z_3^2 (\s^2,0))/3$$ give the same result when applied to $\KnE s_1$. We put our results for the first four $s_1$, when ordered according to their discriminant, for $n=3$ and 5 in Tables 13 through 16. In Table 16 the number $e(5,M_\pi^E)^{-1}$ is given by $$-2^5\cdot3^{10}\cdot5^{-2}\cdot13^{4}\cdot(7+3\z_3)\cdot(68-43\z_3)\cdot(1547202-1603487\z_3)\cdot(a+b\z_3)$$ with $$\begin{aligned}
{1}
a & = 8482255892311139091186217686741233 
\\
\intertext{and}
b & = 3527440500058817421018094757947617
\,,
\end{aligned}$$ presumably because we experimentally found a subgroup of $\Kn s_1$ that is not close to actually being $K_{2n-1}(s_1)$. In all cases $\Lp p n \chi_\pi\tensor\omega_p^{1-n} {\Q}$ is a unit in $E\tensor_\Q\Qp$, and when we write the equivalent of [\[quotientexp\]](#quotientexp){reference-type="eqref" reference="quotientexp"} in the form $1 \tensor \a  + \z_3 \tensor \b$ then we find that $\a-1$ and $\b$ are $O(p^{N(p)})$ with $N(2) \ge 50$, $N(3) \ge 24$, $N(5) \ge 20$, $N(7) \ge 14$ and $N(11) \ge 12$, with in this case the precision bounded by that of the $R_{n,p}(M_\pi^E)$. Since $e(n,M_\pi^E)$, $D(M_\pi^E)^{1/2,p}$ and $\Eul_p(n, \chi_\pi\tensor\id,\Q)$ are units in $E\tensor_\Q\Qpbar$ this also shows that $R_{n,p}(M_\pi^E)$ is a unit in $E\tensor_\Q F$, as conjectured in Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(4).

Such calculations were also carried out for the next four such $s_1$ with similar results.
:::

::: remark
By Proposition [\[abelprop\]](#abelprop){reference-type="ref" reference="abelprop"} and Remark [\[consequencesremark\]](#consequencesremark){reference-type="ref" reference="consequencesremark"}(1), the conjecture for $\pi$ in Example [\[S3computation\]](#S3computation){reference-type="ref" reference="S3computation"} is equivalent to Conjecture [\[pborel\]](#pborel){reference-type="ref" reference="pborel"} for the field $k_1$ in the example. The same statement holds for $\pi$ and $k_1$ in Example [\[D8realcomputation\]](#D8realcomputation){reference-type="ref" reference="D8realcomputation"} below.
:::

::: remark
[]{#constantremark label="constantremark"} In the tables we have also included the value of the constant $C(\chi_\pi\tensor\id) = C(\chi_\pi^\vee\tensor\id)$ in the functional equation [\[newfuneq\]](#newfuneq){reference-type="eqref" reference="newfuneq"} of $\L s {\chi_\pi\tensor\id} {\Q}$ to make possible a comparison between its prime factors and those of $e(n,M_\pi)$. Namely, for the $D(M_\pi^E)^{1/2,\infty}$ used in the calculations, the $e_n$ in [\[edef\]](#edef){reference-type="eqref" reference="edef"} (which in our case are independent of $n$) are as follows.

::: center
$$\begin{array}{cc@{\qquad\quad}cc@{\qquad\quad}cc@{\qquad\quad}cc}
\hline
\vphantom{p_{p_p}}\vphantom{b^{b^b}}\hbox{Table} & e_n & \hbox{Table} & e_n &\hbox{Table} & e_n & \hbox{Table} & e_n \cr
\hline
\vphantom{p_{p_p}}\vphantom{b^{b^b}}
1 & 3 & 5 & 4 & 9 & 4 & 13 & 1\tensor 9 +\z_3\tensor 9
\cr
\vphantom{p_{p_p}}\vphantom{b^{b^b}}
2 & 3 & 6 & 4 & 10 & 4 & 14 & 1\tensor 9 +\z_3\tensor 9
\cr
\vphantom{p_{p_p}}\vphantom{b^{b^b}}
3 & 3 & 7 & 4 & 11 & \hbox to 20.8 pt{$-4$\hfill} & 15 & 1\tensor 0 +\z_3\tensor 9
\cr
\vphantom{p_{p_p}}\vphantom{b^{b^b}}
4 & 3 & 8 & 4 & 12 & 4 & 16 & 1\tensor 0 +\z_3\tensor (-9)
\cr
\hline
\end{array}$$
:::

As can be seen from these values and Tables 1-16, in the number $$\delta_n e_n ((n-1)!/2)^m C(\chi_\pi^\vee\tensor\id)^{n-1} e(n,M_\pi^E)$$ of [\[newe\]](#newe){reference-type="eqref" reference="newe"} the larger prime factors occurring in $e(n,M_\pi^E)$ are often cancelled by those of $C(\chi_\pi^\vee\tensor\id)^{n-1}$. This suggests that the formulation of Beilinson's conjecture at $s=1-n$ normally involves simpler prime factors in $E^*$ than the formulation at $s=n$ in Conjecture [\[motiveconjecture\]](#motiveconjecture){reference-type="ref" reference="motiveconjecture"}(1), with the remaining complicated factors in our examples quite possibly due to an awkward choice of basis for $\KMn M_\pi^E$.
:::
