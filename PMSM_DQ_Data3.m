%Motor
R1=0.24;            %R statornoy obmotki
L1=0.001015;        %Induktivnost statornoy obmotki
T1=L1/R1;           %Postoyannaya vremeni statora
p=4;                %chislo par polusov
wf=0.06784*0.8;     %potok ot postoyannih magnitov max
cm=1.5*p*wf;        %postoyannaya momenta
J1=0.00048;          %moment inerciy 1-massa
J2=0.00096;          %moment inerciy 2-mass
J = 0.00048*1; % Момент инерции
%Flux Controller
Mn=7.14;                            %nominalniy moment
wn=(5000*pi)/30;                    %nominalnaya skorost
En=p*wn*wf;                         %nominalnaya EDS vrasheniya
iqn=Mn/cm;                          %sostavlyaushaya nominalnogo toka
idmin=-wf/L1;                       %tipovoy tok polya
Imax=iqn;                           %nominalniy tok
Umax=sqrt((p*wn*L1*iqn)^2+(En^2));  %nominalnoye napryazhenie
wcr=((Umax/p)/(wf-L1*iqn))*(30/pi); %kriticheskaya skorost
Pwa=1.5*Umax*Imax;                   %polnaya moschost
 
%Invertor
Udc=Umax*sqrt(3);               %U schini
ki=Udc/5;                       %KU invertora
f_inv=5e3;                      %chastota invertora 5 kGC
Ti=1/f_inv;                     %postoyannaya vremeni invertora
 
%PI current
kdt=1;                          %koefficient datchika toka
Trt=T1;                         %postoyannaya vremeni RT
Tmu_i=Ti;                       %malaya postoyannaya vremeni RT
b=(Trt*R1)/(2*Tmu_i*ki*kdt);    %KU PI-regulatora toka
 
%PI speed
kds=1;                          %koefficient datchika skorosti
Tmu_w=2*Tmu_i;                  %malaya postoyannaya vremeni
%Trt2=4*T1;                   %postoyannaya vremeni RC dlya upru-gosti
Trt2=4*Tmu_w;                 %postoyannaya vremeni RC dlya REG
%b2=(J1)/(2*Tmu_w*kds);       %KU PI- regulatora skorosti
b2=(J1)/(2*Tmu_w*cm*kds);       %KU PI- regulatora skorosti
 
%raschety
kdp=1;
Tmu_p=2*Tmu_w;
bp=(((1/2)*Tmu_p)*(kds/kdp));
wop=Tmu_p^(-1);
%ky=ki;
%km=cm;
