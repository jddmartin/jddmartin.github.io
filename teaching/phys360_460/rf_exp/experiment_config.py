# Configuration file used by python program:
#   make_rfexp_schematic_mouseover_pages.py
# to make web-pages with mouseover schematic diagrams for
# Phys 360/460 experiment: 
#   "Radio frequency electronics and frequency stabilization"
# 
# SOME GENERIC STUFF:
webpage_title=('Phys 360/460 Experiment: Radio-frequency electronics'
            ' and frequency stabilization')

device_image_widths={'thumb':250,'page':500}

# PART DESCRIPTIONS:
part_descriptions={} # initialize dictionary
part_descriptions['component_1_part_a']="Component 1, Part A: The voltage controlled oscillator"
part_descriptions['component_1_part_b']="Component 1, Part B: Cavity coupling and quality factor"
part_descriptions['component_1_part_c']="Component 1, Part C: Cavity reflection coefficient phase"
part_descriptions['component_1_part_d']="Component 1, Part D: Stabilization of the VCO to the cavity ..."
part_descriptions['component_2_part_a']="Component 2, Part A: Frequency modulation of the VCO"
part_descriptions['component_2_part_b']="Component 2, Part B: Pound-Drever-Hall error signal generation scheme"
part_descriptions['component_2_part_c']="Component 2, Part C: Implementing the PDH locking scheme using the VCO"

# DEVICE DESCRIPTIONS:
device_descriptions={}; device_long_descriptions={} # initialize dictionaries

device_descriptions['e3630a']="<h2>E3630a dc power supply</h2>"
device_long_descriptions['e3630a']="""\
<h2>E3630a dc power supply</h2>

<p><a href="http://www.home.agilent.com/agilent/product.jspx?cc=CA&lc=eng&ckey=836823&nid=-35678.384187.00&id=836823&pselect=SR.GENERAL">
Agilent E3630A</a>
</p>

<p>A modern physics lab will contain many dc power supplies -- usually not
as fancy as this one.  Some nice features of this unit are adjustable voltages, and current monitoring.
</p>
"""

device_descriptions['e3620a']="<h2>E3620a dc power supply</h2>"
device_long_descriptions['e3620a']="""\
<h2>E3620a dc power supply</h2>

<p><a href="http://www.home.agilent.com/agilent/product.jspx?cc=CA&lc=eng&ckey=838235&nid=-35677.384298.00&id=838235&pselect=SR.GENERAL">
Agilent E3620A</a>
</p>

<p>A modern physics lab will contain many dc power supplies -- usually not
as fancy as this one.  Some nice features of this unit are adjustable voltages, and current monitoring.
</p>
"""

device_descriptions['vco']="""
<h2>Voltage controlled oscillator</h2>
<p>
Minicircuits ZX95-850-S+
</p>
"""
device_long_descriptions['vco']="""\
<h2>Voltage controlled oscillator</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZX95-850-S%2B&x=0&y=0">ZX95-850-S+</a>
</p>
<p>
A 
<a href="http://en.wikipedia.org/wiki/Voltage-controlled_oscillator">
voltage controlled oscillator</a> is an oscillator whose frequency
can be controlled by an externally applied tuning voltage.
The device from the manufacturer has been "connectorized" to
make it easier to use.
</p>
"""

device_descriptions['multimeter']="""\
<h2>Multimeter</h2>
<p>Hewlett-Packard 3478a</p>
"""
device_long_descriptions['multimeter']="""\
<h2>Multimeter</h2>
<p>Hewlett-Packard 
<a href="http://www.home.agilent.com/agilent/product.jspx?id=3478A:epsg:pro&pageMode=OV&pid=3478A:epsg:pro&lc=eng&ct=PRODUCT&cc=CA&pselect=SR.PM-Search%20Results.Overview">
3478a
</a></p>
<p>The test and measurement division of the Hewlett-Packard company 
was "rebranded" Agilent in 1999, presumably to distinguish it from the consumer
product divisions.  
It had an excellent reputation for building quality test equipment.
Despite their age, many Hewlett-Packard instruments are worth obtaining.
</p>
"""

device_descriptions['isolator']="""\
<h2> Isolator </h2>
<p>
Fairview Microwave, P/N SFI8090
</p>
"""
device_long_descriptions['isolator']="""\
<h2> Isolator </h2> 
<p> 
  <a href="http://www.fairviewmicrowave.com"> 
    Fairview Microwave</a> 
  P/N 
  <a href="http://www.fairviewmicrowave.com/pdfParts/SFI8090.PDF">
    SFI8090
  </a>. 
</p>
<p>
An RF 
<a href="http://en.wikipedia.org/wiki/Isolator_%28microwave%29">
isolator</a>
allows transmission of RF energy in one direction but not the
other. It is essentially a <a href="circulator.html">circulator</a> with 
one port terminated.
</p>
"""

device_descriptions['counter']="""\
<h2>Frequency counter</h2>
<p> 
Racal-Dana 1999c
</p>
"""

device_long_descriptions['counter']="""\
<h2>Frequency counter</h2>
<p>
Racal-Dana 1999c
</p>
<p>
A <a href="http://en.wikipedia.org/wiki/Frequency_counter">
frequency counter</a> 
typically counts zero-crossings over a time interval 
measured with its own internal source (typically a crystal oscillator).
The unit is interfaced with a computer through an 
<a href="http://en.wikipedia.org/wiki/GPIB">IEEE-488</a> bus (more
commonly called GPIB).
Racal-Dana made high-quality instruments, but is no longer in business.  
This used counter was bought at Electronic Surplus Industries in Toronto
(an interesting store if you like electronics and test equipment).
If you are interested in more detailed information on this unit, I have
a manual.
</p>
"""

device_descriptions['trombone']="""\
<h2>"Trombone" adjustable air line</h2>
<p>
General Radio, GR 874-LA 
</p>
"""
device_long_descriptions['trombone']="""\
<h2>"Trombone" adjustable air line</h2>
<p>
General Radio, GR 874-LA
</p>
<p>
This is essentially an adjustable coaxial "cable".  By varying the length it is possible to vary the phase relationship between between the input and output.  General Radio is out of business, and similar devices do not seem to be offered any more.   Adapters on either end are used to convert from the unusual <a href="http://en.wikipedia.org/wiki/GR_connector">GR 874</a> connector type to SMA.  If two of these delay lines are attached at one end, the input and output connectors of the composite device remain unchanged in distance to oneanother.  This is the "trombone" configuration.
</p>
"""

device_descriptions['circulator']="""\
<h2>Circulator</h2>
<p>
Fairview Microwave, P/N SFC0780S
</p>
"""
device_long_descriptions['circulator']="""\
<h2>Circulator</h2>
<p>
  <a href="http://www.fairviewmicrowave.com"> 
    Fairview Microwave</a> 
  P/N 
  <a href="http://www.fairviewmicrowave.com/pdfParts/SFC0780S.PDF">
  SFC0780S
  </a>. 
</p>
<p>
A <a href="http://en.wikipedia.org/wiki/Circulator">circulator</a> is a device that passes an RF signal from port 1 to 2, 2 to 3 and 3 to 1.  In this experiment, it allows us to "extract" the reflected RF from the cavity.
</p>
"""

device_descriptions['function_generator']="""\
<h2>Function generator</h2>
<p>
Agilent, 33210A
</p>
"""
device_long_descriptions['function_generator']="""\
<h2>Function generator</h2>
<p>
  Agilent 
  <a href="http://www.home.agilent.com/agilent/product.jspx?id=1407410&pageMode=OV&pid=1407410&lc=eng&ct=PRODUCT&cc=CA&pselect=SR.PM-Search%20Results.Overview">
  33120A
  </a>. 
</p>
<p>
A function generator is a versatile tool for creating various types of repetitive waveforms (sine, triangle(ramp), pulse).  After a multimeter and oscilloscope it is the next most useful piece of equipment for electronics work.
</p>
"""


device_descriptions['oscilloscope']="""\
<h2>Oscilloscope</h2>
<p>
Tektronix, 2012C
</p>
"""
device_long_descriptions['oscilloscope']="""\
<h2>Oscilloscope</h2>
<p>
  Tektronix 
  <a href="http://www2.tek.com/cmswpt/psdetails.lotr?ct=PS&cs=psu&ci=17517&lc=EN">
  2012C
  </a>. 
</p>
<p>
An oscilloscope allows you to look at voltages as a function of time (usually relative to a trigger).  All oscilloscopes are a bit different.  It's important to understand how to trigger the scope.  If you are having trouble (i.e. trying random stuff and not proceeding systematically), then try just hooking scope up to function generator and looking at simple waveforms.  Learning how to use a scope properly is one of the first steps towards becoming an good experimental physicist.
</p>
"""

device_descriptions['diode_detector']="""\
<h2>Diode detector</h2>
<p>
Pasternack, PE8000-50
</p>
"""

device_long_descriptions['diode_detector']="""\
<h2>Diode detector</h2>
<p>
  Pasternack,
  <a href="http://www.pasternack.com/product-50-Ohm-BNC-Detector-100KHz--1000-MHz-PE8000-50-71958.html">
  PE8000-50
  </a>. 
</p>
<p>
The diode detector converts an oscillating RF frequency into a dc output voltage.  However the exact relationship between input power and output voltage is complex.  In this experiment we are roughly working in the regime where the output voltage is proportional to the input power (square-law regime).  For details, please see: <a href="http://www.home.agilent.com/agilent/redirector.jspx?action=ref&cname=AGILENT_EDITORIAL&ckey=1111032&lc=eng&cc=CA&nfr=-536900742.0.00">Schottky Barrier Video Detectors (AN 923)</a> (esp. Fig. 12 "Detector Dynamics Characteristics").
</p>
"""


device_descriptions['sma_cable']="""\
<h2>SMA connectorized coaxial cable</h2>
"""
device_long_descriptions['sma_cable']="""\
<h2>SMA connectorized coaxial cable</h2>
<p>
The connectors on the ends of these cables are the SMA type 
(SubMiniature Version A) which are suitable for much higher frequencies than BNC connectors (up to 18 GHz).  They are not necessary at the 800 MHz frequencies used in this lab -- but many of the components (isolator and circulator) use them, and they have the advantage of being compact.  
</p>
"""

device_descriptions['sma_m_m']="""\
<h2>SMA M-M connector</h2>
"""
device_long_descriptions['sma_m_m']="""\
<h2>SMA M-M (male-male) connector</h2>
<p>
This is essentially a "zero" length SMA cable -- useful for minimizing cable attenuation and delays.
</p>
"""

device_descriptions['bnc_t']="""\
<h2>BNC T connector</h2>
"""
device_long_descriptions['bnc_t']="""\
<h2>BNC T connector</h2>
"""

device_descriptions['splitter_10_to_1000']="""\
<h2>Splitter, 10-1000 MHz</h2>
<p>
Minicircuits ZFSC-2-2+
</p>
"""
device_long_descriptions['splitter_10_to_1000']="""\
<h2>Splitter, 10-1000 MHz</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZFSC-2-2-S%2B&x=15&y=6">ZFSC-2-2+</a>
</p>
<p>
This <a href="http://en.wikipedia.org/wiki/Power_divider">RF splitter</a> divides power that is incident on the "S" port evenly between the "1" and "2" ports.  The S-port has a 50 ohm input impedance.  A simple BNC-T is not suitable for splitting RF signals as the input port would have a 25 ohm impedance (two 50 ohm impedances in parallel), and power would reflect off this discontinuity.
<p>
"""
device_descriptions['mixer_low_freq']="""\
<h2>Mixer</h2>
<p>
Minicircuits ZP-3LH-S+
</p>
"""

device_long_descriptions['mixer_low_freq']="""\
<h2>Mixer</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZP-3LH-S%2B&x=0&y=0">ZP-3LH-S+</a>
</p>
<p>
A <a href="http://en.wikipedia.org/wiki/Frequency_mixer">mixer</a> 
essentially multiplies two input signals.  If the two inputs are of the same frequency, this will produce an output at twice the input frequency, and an output at DC.  The DC component will be proportional to the cosine of the phase angle between the two inputs.  Two signals that are completely in phase will give a maximum dc output, which will reduce to zero as the phase between them is varied to 90 degrees.  We will see a signal of opposite polarity for 180 degree phase difference.  Mixers are an essential part of almost all communication systems (transmitters and receivers) as a way to "translate" RF signals in frequency space.
<p>
"""

device_descriptions['integrator_feedback']="""\
<h2>Integrator Feedback Control</h2>
<p>
Built by UW Science Shops.
</p>
"""
device_long_descriptions['integrator_feedback']="""\
<h2>Integrator Feedback Control</h2>
<p>
A control loop stabilizes a physical quantity using measurement and feedback.  Feedback control of temperature is common:  a thermometer measures the temperature and the heater is adjusted accordingly to bring the measured temperature to the desired temperature.  In this experiment we use feedback to lock the frequency of a voltage controlled oscillator to a cavity resonance.  
</p>
<p>
The difference between the actual physical quantity and the value that we desire is known as the <i>error signal</i>.  The simplest type of control loop is an integrator -- which can be implemented using the classic op-amp integrator circuit.  If the input error signal is zero, the output voltage remains unchanged.  If the error signal goes either positive or negative, the output of the integrator ramps accordingly, until the error signal goes to zero again, at which point integration stops.
</p>
<p>
This integrator control box was built by the Zhen-Wen Wang of the 
<a href="http://www.sts.uwaterloo.ca/index.html">UW Science Shops</a>.
<p>
"""

device_descriptions['pound_integrator_feedback']="""\
<h2>Pound Integrator Feedback Control</h2>
<p>
Built by UW Science Shops.
</p>
"""
device_long_descriptions['pound_integrator_feedback']="""\
<h2>Pound Integrator Feedback Control</h2>
<p>
A control loop stabilizes a physical quantity using measurement and feedback.  Feedback control of temperature is common:  a thermometer measures the temperature and the heater is adjusted accordingly to bring the measured temperature to the desired temperature.  In this experiment we use feedback to lock the frequency of a voltage controlled oscillator to a cavity resonance.  
</p>
<p>
The difference between the actual physical quantity and the value that we desire is known as the <i>error signal</i>.  The simplest type of control loop is an integrator -- which can be implemented using the classic op-amp integrator circuit.  If the input error signal is zero, the output voltage remains unchanged.  If the error signal goes either positive or negative, the output of the integrator ramps accordingly, until the error signal goes to zero again, at which point integration stops.
</p>
<p>
This integrator control box was built by the Zhen-Wen Wang of the 
<a href="http://www.sts.uwaterloo.ca/index.html">UW Science Shops</a>.
<p>
"""

device_descriptions['cavity']="""\
<h2>Cavity</h2>
"""
device_long_descriptions['cavity']="""\
<h2>Cavity</h2>
<p>
Quarter-wavelength transmission line resonator
</p>
<p>
Essentially this cavity is a 77 ohm transmission line with one end open-circuited and the other end shorted.  The lowest frequency resonance of this type of system is corresponds to the length of the line being one quarter of the wavelength.  Pointers to more information on the theory of this resonator are given in the experiment description.
</p>
"""

device_descriptions['coupling_loops']="""\
<h2>Coupling loops</h2>
"""
device_long_descriptions['coupling_loops']="""\
<h2>Coupling loops</h2>
<p>
These loops are used to feed and/or remove energy from the cavity.  They primarily couple to the oscillating magnetic field within the cavity.  Pointers to more information are given in the experiment description. 
</p>
<p> The SMA connector is a commercial part (Emerson 142-0701-491, available from <a href="http://www.digikey.ca/">Digi-Key</a> as P/N J998-ND).  The wire loops are made of #24 AWG copper wire, with enamel insulation.  The copper housing was constructed by the UW Science Shops.
"""

device_descriptions['low_pass_filter']="""\
<h2>Low pass filter</h2>
<p>
Minicircuits BLP-5+
</p>
"""
device_long_descriptions['low_pass_filter']="""\
<h2>Low pass filter</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=BLP-5%2B&x=21&y=17">BLP-5+</a>.
</p>
<p>
This simply blocks high frequencies, while allowing low frequencies (including dc) to pass.
</p>
"""

device_descriptions['mixer_high_freq']="""\
<h2>Mixer</h2>
<p>
Minicircuits ZFM-2-S+
</p>
"""
device_long_descriptions['mixer_high_freq']="""\
<h2>Mixer</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZFM-2-S%2B&x=0&y=0">ZFM-2-S+</a>
</p>
<p>
A <a href="http://en.wikipedia.org/wiki/Frequency_mixer">mixer</a> 
essentially multiplies two input signals.  If the two inputs are of the same frequency, this will produce an output at twice the input frequency, and an output at DC.  The DC component will be proportional to the cosine of the phase angle between the two inputs.  Two signals that are completely in phase will give a maximum dc output, which will reduce to zero as the phase between them is varied to 90 degrees.  We will see a signal of opposite polarity for 180 degree phase difference.  Mixers are an essential part of almost all communication systems (transmitters and receivers) as a way to "translate" RF signals in frequency space.
<p>
"""

device_descriptions['amplifier']="""\
<h2>Amplifier</h2>
<p>
Minicircuits ZJL-4G+
</p>
"""
device_long_descriptions['amplifier']="""\
<h2>Amplifier</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZJL-4G%2B&x=29&y=19">ZJL-4G+</a>
</p>
<p>
Amplifier description ...
<p>
"""

device_descriptions['bias_t']="""\
<h2>Bias-t</h2>
<p>
Minicircuits ZFBT-4R2G+
</p>
"""
device_long_descriptions['bias_t']="""\
<h2>Bias-t</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=ZFBT-4R2G%2B&x=0&y=0">ZFBT-4R2G+</a>
</p>
<p>
Bias-t description ...
<p>
"""

device_descriptions['attenuator_xx_db']="""\
<h2>Attenuators</h2>
<p>
Minicircuits HAT-3+ etc...
</p>
"""
device_long_descriptions['attenuator_xx_db']="""\
<h2>Attenuators</h2>
<p>
<a href="http://www.minicircuits.com">Minicircuits</a>
<a href="http://www.minicircuits.com/cgi-bin/modelsearch?model=HAT-3%2B&x=0&y=0">HAT-3+</a>
</p>
<p>
Attenuator description ...
<p>
"""

device_descriptions['ten_mhz_source']="""\
<h2>10 MHz source</h2>
<p>
Built by UW Science Shops
</p>
"""
device_long_descriptions['ten_mhz_source']="""\
<h2>10 MHz source</h2>
<p>
10 MHz source description ...
<p>
"""

device_descriptions['fifty_ohm_terminator']="""\
<h2>50 ohm terminator</h2>
<p>INMET 3032
</p>
"""
device_long_descriptions['fifty_ohm_terminator']="""\
<h2>50 ohm terminator</h2>
<p>INMET 3032
</p>
<p>
50 ohm terminator description ...
<p>
"""

device_descriptions['diode_load']="""\
<h2>5 kohm load</h2>
"""
device_long_descriptions['diode_load']="""\
<h2>5 kohm load</h2>
<p>
5 kohm load purpose ...
<p>
"""


