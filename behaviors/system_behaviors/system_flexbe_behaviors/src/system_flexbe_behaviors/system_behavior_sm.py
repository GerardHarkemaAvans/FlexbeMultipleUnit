#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from unit_1_flexbe_behaviors.unit_1_behavior_sm import unit_1_behaviorSM
from unit_2_flexbe_behaviors.unit_2_behavior_sm import unit_2_behaviorSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 21 2021
@author: Gerard Harkema
'''
class system_behaviorSM(Behavior):
	'''
	Gedrag van het gehele systeem
	'''


	def __init__(self):
		super(system_behaviorSM, self).__init__()
		self.name = 'system_behavior'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(unit_1_behaviorSM, 'unit_1_behavior')
		self.add_behavior(unit_2_behaviorSM, 'unit_2_behavior')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:294 y:173, x:633 y:41
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:113 y:34
			OperatableStateMachine.add('unit_1_behavior',
										self.use_behavior(unit_1_behaviorSM, 'unit_1_behavior'),
										transitions={'finished': 'unit_2_behavior', 'failed': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:357 y:33
			OperatableStateMachine.add('unit_2_behavior',
										self.use_behavior(unit_2_behaviorSM, 'unit_2_behavior'),
										transitions={'finished': 'failed', 'failed': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
