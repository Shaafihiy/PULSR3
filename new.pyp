<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="new" version="2.0">
	<nodes>
		<node id="0" name="Import XDF" position="(44.0, 390.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="69602ac6-132b-442c-bdf1-4abbfaf9b84a" version="1.2.1" />
		<node id="1" name="Select Range" position="(312.0, 136.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owselectrange.OWSelectRange" title="Select Range" uuid="7a605281-5ff0-47de-9d82-6e7be92b007b" version="1.1.0" />
		<node id="2" name="Segmentation" position="(471.0, 136.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="e8e052da-a709-46a1-8d7c-033a4f3ac53e" version="1.0.2" />
		<node id="3" name="LSL Input" position="(-20.0, 209.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="41f48a00-25a9-41c8-b95a-5f271f30bcbe" version="1.5.1" />
		<node id="4" name="LSL Output" position="(254.0, 384.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="a681e2f6-d179-486a-b556-68f9e5f6d894" version="1.4.2" />
		<node id="5" name="LSL Output" position="(891.0, 156.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output (1)" uuid="7d0a56d9-b86c-48f2-9208-84419ceda7d0" version="1.4.2" />
		<node id="6" name="Common Spatial Patterns" position="(588.0, 124.0)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="b912da2a-046b-460e-90d3-604d148dbae8" version="1.0.0" />
		<node id="7" name="FIR Filter" position="(397.0, 130.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="346f519d-4935-4e70-b44b-84a9cda367a3" version="1.1.0" />
		<node id="8" name="Variance" position="(689.0, 125.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="41527f7e-2a40-4bbd-a99d-c3542e73d8dd" version="1.0.0" />
		<node id="9" name="Override Axis" position="(1141.0, 492.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="16c85124-7c45-4790-ac40-e9482f6ce4ff" version="1.4.2" />
		<node id="10" name="Stream Data" position="(164.0, 384.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="49929f2e-368e-4790-9967-a77977c41ada" version="1.2.1" />
		<node id="11" name="Assign Target Values" position="(225.0, 130.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values" uuid="7d99e3e7-05e9-4b4d-b9c1-e474a99f68cf" version="1.0.1" />
		<node id="12" name="Inject Calibration Data" position="(149.0, 130.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="f805b42f-69e1-4c7c-a948-30ed477eddc1" version="1.0.0" />
		<node id="13" name="Import XDF" position="(-24.0, 33.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF (1)" uuid="86cac253-e27f-4d7f-a34c-7c5f63a9aeb3" version="1.2.1" />
		<node id="14" name="Logistic Regression" position="(836.0, 264.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="bda967de-7990-4b0c-ac4b-3ed2704c3e22" version="1.1.0" />
		<node id="15" name="Export to CSV" position="(779.0, 128.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owexportcsv.OWExportCSV" title="Export to CSV" uuid="9546432a-b8f3-4c82-ad4b-d0051f3c6134" version="1.1.1   " />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="10" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Streaming Data" sink_node_id="12" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Calib Data" sink_node_id="12" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="14" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="8" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWDoAAABDOi9Vc2Vycy9BRE1JTi9EZXNrdG9wL3Bvc2UgZXN0aW1hdGUvU2hh
Zml1d2l0aE1hcmtlcnMueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhYEQAAAGhhbmRs
ZV9jbG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAAAG1heF9tYXJr
ZXJfbGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgIAAAAbWV0YWRhdGFxDn1xD1gSAAAAcmVvcmRl
cl90aW1lc3RhbXBzcRCJWA4AAAByZXRhaW5fc3RyZWFtc3ERaA1YEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29yZXEUWAoAAABRQnl0
ZUFycmF5cRVDQgHZ0MsAAwAAAAAB9gAAAOEAAANfAAAB2AAAAfcAAAEAAAADXgAAAdcAAAAAAAAA
AAVWAAAB9wAAAQAAAANeAAAB13EWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtwb2ludHEaiVgLAAAA
dXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWB8AAABhcHBseV90aW1lX3NlbGVjdGlv
bl90b19tYXJrZXJzcQKJWAQAAABheGlzcQNYBAAAAHRpbWVxBFgIAAAAbWV0YWRhdGFxBX1xBlgT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDUu
UXRDb3JlcQlYCgAAAFFCeXRlQXJyYXlxCkNCAdnQywADAAAAAAH2AAAA+wAAA18AAAG/AAAB9wAA
ARoAAANeAAABvgAAAAAAAAAABVYAAAH3AAABGgAAA14AAAG+cQuFcQyHcQ1ScQ5YCQAAAHNlbGVj
dGlvbnEPWAEAAAA6cRBYDgAAAHNldF9icmVha3BvaW50cRGJWAQAAAB1bml0cRJYBwAAAGluZGlj
ZXNxE3Uu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgIAAAAbWV0YWRhdGFxA31xBFgPAAAAb25saW5lX2Vwb2NoaW5ncQVYDQAAAG1hcmtlci1s
b2NrZWRxBlgNAAAAc2FtcGxlX29mZnNldHEHSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxCGNz
aXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ1LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5cQtD
QgHZ0MsAAwAAAAAB9gAAAOQAAANfAAAB1QAAAfcAAAEDAAADXgAAAdQAAAAAAAAAAAVWAAAB9wAA
AQMAAANeAAAB1HEMhXENh3EOUnEPWA4AAABzZWxlY3RfbWFya2Vyc3EQWA0AAAAodXNlIGRlZmF1
bHQpcRFYDgAAAHNldF9icmVha3BvaW50cRKJWAsAAAB0aW1lX2JvdW5kc3ETXXEUKEr/////SwFl
WAcAAAB2ZXJib3NlcRWJdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCgAAAGRhdGFfZHR5cGVxA1gHAAAAZmxvYXQ2
NHEEWAsAAABkaWFnbm9zdGljc3EFiVgTAAAAZXhjbHVkZV9kZXNjX2ZpZWxkc3EGXXEHWAwAAABt
YXJrZXJfcXVlcnlxCFgYAAAAbmFtZT0nT3V0U3RyZWFtLW1hcmtlcnMncQlYDAAAAG1heF9ibG9j
a2xlbnEKTQAEWAoAAABtYXhfYnVmbGVucQtLHlgMAAAAbWF4X2NodW5rbGVucQxLAFgIAAAAbWV0
YWRhdGFxDX1xDlgMAAAAbm9taW5hbF9yYXRlcQ9YDQAAACh1c2UgZGVmYXVsdClxEFgJAAAAb21p
dF9kZXNjcRGJWA8AAABwcmVhbGxvY19idWZmZXJxEohYDgAAAHByb2NfY2xvY2tzeW5jcROIWA0A
AABwcm9jX2Rlaml0dGVycRSJWA8AAABwcm9jX21vbm90b25pemVxFYlYDwAAAHByb2NfdGhyZWFk
c2FmZXEWiVgFAAAAcXVlcnlxF1gQAAAAbmFtZT0nT3V0U3RyZWFtJ3EYWAcAAAByZWNvdmVycRmI
WBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEaRz/gAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRtjc2lwCl91bnBpY2tsZV90eXBlCnEcWAwAAABQeVF0NS5RdENvcmVxHVgKAAAAUUJ5dGVB
cnJheXEeQ0IB2dDLAAMAAAAAASMAAABUAAACjAAAAZYAAAEkAAAAcwAAAosAAAGVAAAAAAAAAAAF
VgAAASQAAABzAAACiwAAAZVxH4VxIIdxIVJxIlgOAAAAc2V0X2JyZWFrcG9pbnRxI4l1Lg==
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgRAAAAT3V0U3RyZWFtLW1hcmtlcnNxB1gQAAAAbWFya2VyX3NvdXJj
ZV9pZHEIWAAAAABxCVgMAAAAbWF4X2J1ZmZlcmVkcQpLPFgIAAAAbWV0YWRhdGFxC31xDFgXAAAA
bnVtZXJpY19sYWJlbF9wcmVjaXNpb25xDUsBWBgAAABudW1lcmljX21hcmtlcl9wcmVjaXNpb25x
DksDWBcAAAByZXNldF9pZl9sYWJlbHNfY2hhbmdlZHEPiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRy
eXEQY3NpcApfdW5waWNrbGVfdHlwZQpxEVgMAAAAUHlRdDUuUXRDb3JlcRJYCgAAAFFCeXRlQXJy
YXlxE0NCAdnQywADAAAAAALhAAAAqAAABEgAAAJ1AAAC4QAAAKgAAARIAAACdQAAAAAAAAAABVYA
AALhAAAAqAAABEgAAAJ1cRSFcRWHcRZScRdYDAAAAHNlbmRfbWFya2Vyc3EYiFgJAAAAc2VwYXJh
dG9ycRlYAQAAAC1xGlgOAAAAc2V0X2JyZWFrcG9pbnRxG4lYCQAAAHNvdXJjZV9pZHEcWA0AAABt
eXNvdXJjZWlkMjM0cR1YBQAAAHNyYXRlcR5YDQAAACh1c2UgZGVmYXVsdClxH1gLAAAAc3RyZWFt
X25hbWVxIFgJAAAAT3V0U3RyZWFtcSFYCwAAAHN0cmVhbV90eXBlcSJYAwAAAEVFR3EjWBMAAAB1
c2VfZGF0YV90aW1lc3RhbXBzcSSIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0aW9ucSWJdS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYEwAA
AGtlZXBfc2luZ2xldG9uX2F4ZXNxA4lYDAAAAG1hcmtlcl9maWVsZHEEWAYAAABNYXJrZXJxBVgL
AAAAbWFya2VyX25hbWVxBlgSAAAAcHJvYlN0cmVhbS1tYXJrZXJzcQdYEAAAAG1hcmtlcl9zb3Vy
Y2VfaWRxCFgKAAAAbXlzb3VyY2VpZHEJWAwAAABtYXhfYnVmZmVyZWRxCks8WAgAAABtZXRhZGF0
YXELfXEMWBcAAABudW1lcmljX2xhYmVsX3ByZWNpc2lvbnENSwFYGAAAAG51bWVyaWNfbWFya2Vy
X3ByZWNpc2lvbnEOSwNYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQ+JWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NS5RdENvcmVxElgK
AAAAUUJ5dGVBcnJheXETQ0IB2dDLAAMAAAAAAfcAAACFAAADXgAAAlIAAAH3AAAAhQAAA14AAAJS
AAAAAAAAAAAFVgAAAfcAAACFAAADXgAAAlJxFIVxFYdxFlJxF1gMAAAAc2VuZF9tYXJrZXJzcRiI
WAkAAABzZXBhcmF0b3JxGVgBAAAALXEaWA4AAABzZXRfYnJlYWtwb2ludHEbiVgJAAAAc291cmNl
X2lkcRxYCwAAAHNvdXJjZWlkMjM0cR1YBQAAAHNyYXRlcR5YDQAAACh1c2UgZGVmYXVsdClxH1gL
AAAAc3RyZWFtX25hbWVxIFgKAAAAcHJvYlN0cmVhbXEhWAsAAABzdHJlYW1fdHlwZXEiWAMAAABF
RUdxI1gTAAAAdXNlX2RhdGFfdGltZXN0YW1wc3EkiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlv
bnEliXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgIAAAAbWV0YWRhdGFxBH1xBVgDAAAAbm9mcQZLCFgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDUuUXRDb3JlcQlYCgAAAFFCeXRl
QXJyYXlxCkNCAdnQywADAAAAAAH2AAABHQAAA18AAAGcAAAB9wAAATwAAANeAAABmwAAAAAAAAAA
BVYAAAH3AAABPAAAA14AAAGbcQuFcQyHcQ1ScQ5YDgAAAHNldF9icmVha3BvaW50cQ+JdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsFSwhLHksgZVgIAAAAbWV0YWRhdGFxCX1xClgNAAAAbWluaW11
bV9waGFzZXELiFgEAAAAbW9kZXEMWAgAAABiYW5kcGFzc3ENWAUAAABvcmRlcnEOWA0AAAAodXNl
IGRlZmF1bHQpcQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlja2xlX3R5cGUK
cRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAAAAAB9gAAAQcA
AANfAAABswAAAfcAAAEmAAADXgAAAbIAAAAAAAAAAAVWAAAB9wAAASYAAANeAAABsnEUhXEVh3EW
UnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgKAAAAc3RvcF9hdHRlbnEZR0BJAAAAAAAAdS4=
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWAQAAABheGlzcQFYCAAAAGluc3RhbmNlcQJYEgAAAGRlZ3JlZXNfb2ZfZnJlZWRvbXED
SwBYEgAAAGZvcmNlX2ZlYXR1cmVfYXhpc3EEiVgIAAAAbWV0YWRhdGFxBX1xBlgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEHY3NpcApfdW5waWNrbGVfdHlwZQpxCFgMAAAAUHlRdDUuUXRDb3JlcQlY
CgAAAFFCeXRlQXJyYXlxCkNCAdnQywADAAAAAAH2AAABHQAAA18AAAGcAAAB9wAAATwAAANeAAAB
mwAAAAAAAAAABVYAAAH3AAABPAAAA14AAAGbcQuFcQyHcQ1ScQ5YDgAAAHNldF9icmVha3BvaW50
cQ+JdS4=
</properties>
		<properties format="literal" node_id="9">{'axis_occurrence': 0, 'carry_over_names': True, 'carry_over_numbers': True, 'custom_label': '', 'decimals': 3, 'init_data': '(use default)', 'join_format': '{new}', 'keep_other_arrays': False, 'keep_props': False, 'metadata': {}, 'new_axis': 'space', 'old_axis': 'feature', 'only_signals': True, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'verbosity': 0}</properties>
		<properties format="literal" node_id="10">{'data_dtype': 'float64', 'hitch_probability': 0.0, 'jitter_percent': 5, 'log_progress': False, 'looping': True, 'metadata': {}, 'randseed': 34535, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'speedup': 1.0, 'start_pos': 0.0, 'timestamp_jitter': 0.0, 'timing': 'wallclock', 'update_interval': 0.04}</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYBAAAAHJlc3RxB0sA
WA8AAABhY3RpdmVfbW92ZW1lbnRxCEsAWAUAAABzb3VuZHEJSwBYCQAAAGV5ZS1ibGlua3EKSwBY
EAAAAGltYWdpbmVfbW92ZW1lbnRxC0sBdVgOAAAAbWFwcGluZ19mb3JtYXRxDFgGAAAAY29tcGF0
cQ1YCAAAAG1ldGFkYXRhcQ59cQ9YEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlj
a2xlX3R5cGUKcRFYDAAAAFB5UXQ1LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDQgHZ0MsAAwAA
AAAB9gAAAQcAAANfAAABswAAAfcAAAEmAAADXgAAAbIAAAAAAAAAAAVWAAAB9wAAASYAAANeAAAB
snEUhXEVh3EWUnEXWA4AAABzZXRfYnJlYWtwb2ludHEYiVgRAAAAc3VwcG9ydF93aWxkY2FyZHNx
GYlYCwAAAHVzZV9udW1iZXJzcRqJWAcAAAB2ZXJib3NlcRuJdS4=
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiVgIAAAAbWV0YWRhdGFxAn1xA1gT
AAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDUu
UXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0NCAdnQywADAAAAAAH2AAABHwAAA18AAAGbAAAB9wAA
AT4AAANeAAABmgAAAAAAAAAABVYAAAH3AAABPgAAA14AAAGacQiFcQmHcQpScQtYDgAAAHNldF9i
cmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWDoAAABDOi9Vc2Vycy9BRE1JTi9EZXNrdG9wL3Bvc2UgZXN0aW1hdGUvU2hh
Zml1d2l0aE1hcmtlcnMueGRmcQhYEwAAAGhhbmRsZV9jbG9ja19yZXNldHNxCYhYEQAAAGhhbmRs
ZV9jbG9ja19zeW5jcQqIWBUAAABoYW5kbGVfaml0dGVyX3JlbW92YWxxC4hYDgAAAG1heF9tYXJr
ZXJfbGVucQxYDQAAACh1c2UgZGVmYXVsdClxDVgIAAAAbWV0YWRhdGFxDn1xD1gSAAAAcmVvcmRl
cl90aW1lc3RhbXBzcRCJWA4AAAByZXRhaW5fc3RyZWFtc3ERaA1YEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxEmNzaXAKX3VucGlja2xlX3R5cGUKcRNYDAAAAFB5UXQ1LlF0Q29yZXEUWAoAAABRQnl0
ZUFycmF5cRVDQgHZ0MsAAwAAAAAB9gAAAOEAAANfAAAB2AAAAfcAAAEAAAADXgAAAdcAAAAAAAAA
AAVWAAAB9wAAAQAAAANeAAAB13EWhXEXh3EYUnEZWA4AAABzZXRfYnJlYWtwb2ludHEaiVgLAAAA
dXNlX2NhY2hpbmdxG4lYDwAAAHVzZV9zdHJlYW1uYW1lc3EciVgHAAAAdmVyYm9zZXEdiXUu
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYDQAA
ACh1c2UgZGVmYXVsdClxBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABk
b250X3Jlc2V0X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWA8AAABmZWF0dXJlX3Nj
YWxpbmdxClgEAAAAbm9uZXELWAwAAABpbmNsdWRlX2JpYXNxDIhYDwAAAGluaXRpYWxpemVfb25j
ZXENiFgJAAAAbDFfcmF0aW9zcQ5oBVgIAAAAbWF4X2l0ZXJxD0tkWAgAAABtZXRhZGF0YXEQfXER
WAoAAABtdWx0aWNsYXNzcRJYBAAAAGF1dG9xE1gJAAAAbnVtX2ZvbGRzcRRLBVgIAAAAbnVtX2pv
YnNxFUsBWA0AAABwcm9iYWJpbGlzdGljcRaIWAsAAAByYW5kb21fc2VlZHEXTTkwWAsAAAByZWd1
bGFyaXplcnEYWAIAAABsMnEZWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRpjc2lwCl91bnBpY2ts
ZV90eXBlCnEbWAwAAABQeVF0NS5RdENvcmVxHFgKAAAAUUJ5dGVBcnJheXEdQ0IB2dDLAAMAAAAA
AfYAAADvAAADXwAAAcsAAAH3AAABDgAAA14AAAHKAAAAAAAAAAAFVgAAAfcAAAEOAAADXgAAAcpx
HoVxH4dxIFJxIVgNAAAAc2VhcmNoX21ldHJpY3EiWAgAAABhY2N1cmFjeXEjWA4AAABzZXRfYnJl
YWtwb2ludHEkiVgGAAAAc29sdmVycSVYBAAAAGF1dG9xJlgJAAAAdG9sZXJhbmNlcSdHPxo24usc
Qy1YCQAAAHZlcmJvc2l0eXEoSwB1Lg==
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWBAAAABheGlzX2Rlc2NyaXB0aW9ucQFYAAAAAHECWA0AAABjbG91ZF9hY2NvdW50cQNo
AlgMAAAAY2xvdWRfYnVja2V0cQRoAlgRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgCWAoAAABjbG91
ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gIAAAAY29sX2F4aXNxCFgFAAAAc3BhY2VxCVgNAAAAY29s
dW1uX2hlYWRlcnEKiFgIAAAAZmlsZW5hbWVxC1gaAAAAQzovVXNlcnMvQURNSU4vRGVza3RvcC9i
Y2lxDFgIAAAAbWV0YWRhdGFxDX1xDlgLAAAAb3V0cHV0X3Jvb3RxD1gIAAAAdGV4dC5jc3ZxEFgI
AAAAcm93X2F4aXNxEVgJAAAAZnJlcXVlbmN5cRJYCgAAAHJvd19oZWFkZXJxE4hYEwAAAHNhdmVk
V2lkZ2V0R2VvbWV0cnlxFGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ1LlF0Q29yZXEW
WAoAAABRQnl0ZUFycmF5cRdDQgHZ0MsAAwAAAAAB9gAAAKgAAANfAAACEQAAAfcAAADHAAADXgAA
AhAAAAAAAAAAAAVWAAAB9wAAAMcAAANeAAACEHEYhXEZh3EaUnEbWA4AAABzZXRfYnJlYWtwb2lu
dHEciXUu
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node11",
            "data",
            "node5",
            "data"
        ],
        [
            "node1",
            "data",
            "node11",
            "data"
        ],
        [
            "node4",
            "data",
            "node13",
            "streaming_data"
        ],
        [
            "node14",
            "data",
            "node13",
            "calib_data"
        ],
        [
            "node13",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node2",
            "data"
        ],
        [
            "node2",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ],
        [
            "node15",
            "data",
            "node6",
            "data"
        ],
        [
            "node9",
            "data",
            "node16",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/ADMIN/Desktop/pose estimate/ShafiuwithMarkers.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "69602ac6-132b-442c-bdf1-4abbfaf9b84a"
        },
        "node10": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "decimals": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "init_data": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "join_format": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "{new}"
                },
                "keep_other_arrays": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_props": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "new_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "16c85124-7c45-4790-ac40-e9482f6ce4ff"
        },
        "node11": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "log_progress": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "49929f2e-368e-4790-9967-a77977c41ada"
        },
        "node12": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "active_movement": 0,
                        "eye-blink": 0,
                        "imagine_movement": 1,
                        "rest": 0,
                        "sound": 0
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "7d99e3e7-05e9-4b4d-b9c1-e474a99f68cf"
        },
        "node13": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f805b42f-69e1-4c7c-a948-30ed477eddc1"
        },
        "node14": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/ADMIN/Desktop/pose estimate/ShafiuwithMarkers.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_caching": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "86cac253-e27f-4d7f-a34c-7c5f63a9aeb3"
        },
        "node15": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "feature_scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "none"
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "l1_ratios": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "auto"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "bda967de-7990-4b0c-ac4b-3ed2704c3e22"
        },
        "node16": {
            "class": "ExportCSV",
            "module": "neuropype.nodes.file_system.ExportCSV",
            "params": {
                "axis_description": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "col_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "space"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/ADMIN/Desktop/bci"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "text.csv"
                },
                "row_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "frequency"
                },
                "row_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "9546432a-b8f3-4c82-ad4b-d0051f3c6134"
        },
        "node2": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "apply_time_selection_to_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "selection": {
                    "customized": false,
                    "type": "Port",
                    "value": ":"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "7a605281-5ff0-47de-9d82-6e7be92b007b"
        },
        "node3": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        -1,
                        1
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e8e052da-a709-46a1-8d7c-033a4f3ac53e"
        },
        "node4": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "data_dtype": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "float64"
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_desc_fields": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='OutStream-markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "omit_desc": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "prealloc_buffer": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_clocksync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "proc_dejitter": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_monotonize": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "proc_threadsafe": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='OutStream'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "41f48a00-25a9-41c8-b95a-5f271f30bcbe"
        },
        "node5": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "mysourceid234"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a681e2f6-d179-486a-b556-68f9e5f6d894"
        },
        "node6": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "keep_singleton_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "probStream-markers"
                },
                "marker_source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "mysourceid"
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "numeric_label_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "numeric_marker_precision": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "separator": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "-"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "sourceid234"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "probStream"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "7d0a56d9-b86c-48f2-9208-84419ceda7d0"
        },
        "node7": {
            "class": "CommonSpatialPatterns",
            "module": "neuropype.nodes.neural.CommonSpatialPatterns",
            "params": {
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "nof": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 8
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "b912da2a-046b-460e-90d3-604d148dbae8"
        },
        "node8": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        5,
                        8,
                        30,
                        32
                    ]
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "346f519d-4935-4e70-b44b-84a9cda367a3"
        },
        "node9": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "metadata": {
                    "customized": false,
                    "type": "DictPort",
                    "value": {}
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "41527f7e-2a40-4bbd-a99d-c3542e73d8dd"
        }
    },
    "version": 1.1
}</patch>
</scheme>
