# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
#tests = [ {'description': 'This test will run first.',
 #   'steps': [ {'inputs': [('PINA',<val>)], 'iterations': 1 } ],
  #  'expected': [('PORT',<val>)],
   # },
    #{'description': 'This test will run second.',
    #'steps': [ {'inputs': [('PIN', <val>)],'iterations': 1}, # Set PIN to val then run one iteration
#        {'inputs': [('PIN',<val>)], 'time': 300 }, # Set PIN to val then run 300 ms
#        {'inputs': [('PIN',<val>)], 'iterations': 1, 'expected': [('PORT',<val>)]}, 
#        {'inputs': [('PIN',<val>)], 'time': 600}, ],
#    'expected': [('PORT',<val>)],
#    },
#    ]

tests = [ {'description': 'PINA: 0x66, PINB: 0x36, PINC: 0x05(Unbalanced) => PORTd: 0x2B',
	'steps': [ {'inputs': [('PINA',0x66), ('PINB', 0x36), ('PINC', 0x05)], 'iterations': 5 } ],
	'expected': [('PORTD',0x2B)],
	},
	{'description': 'PINA: 0x32, PINB: 0x32, PINC: 0x32 => PORTd: 0x25',
	'steps': [ {'inputs': [('PINA',0x32), ('PINB', 0x32), ('PINC', 0x32)], 'iterations': 5 } ],
	'expected': [('PORTD',0x2F)],
	},
	{'description': 'PINA: 0x05, PINB: 0x05, PINC: 0x05 => PORTd: 0x03',
	'steps': [ {'inputs': [('PINA',0x05), ('PINB', 0x05), ('PINC', 0x05)], 'iterations': 5 } ],
	'expected': [('PORTD',0x03)],
	},

	
]
#watch = ['PORTB']
# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

