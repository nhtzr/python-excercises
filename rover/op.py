from typing import Iterable

from .data import Instruction, RoverState, DIRECTION_TO_COORDINATE_ID, VALID_DIRECTIONS, Direction


def execute_instructions(state: RoverState, instructions: Iterable[Instruction], stderr=None):
    curr_state: RoverState = state._replace()
    for instruction in instructions:
        print(instruction, file=stderr)
        if instruction.flag == 'M':
            c_id = DIRECTION_TO_COORDINATE_ID[curr_state.direction.flag]
            new_coordinate = curr_state.coordinate._replace(
                x=curr_state.coordinate.x + c_id.x,
                y=curr_state.coordinate.y + c_id.y)

            curr_state = curr_state._replace(coordinate=new_coordinate)
        elif instruction.flag in ('L', 'R'):
            new_direction = rotate(curr_state, instruction)

            curr_state = curr_state._replace(direction=new_direction)

        print(curr_state, file=stderr)
    return curr_state


def rotate(state: RoverState, instruction: Instruction):
    direction_length = len(VALID_DIRECTIONS)
    curr_direction = VALID_DIRECTIONS.index(state.direction.flag)

    next_direction_offset = 1 if instruction.flag == 'R' else - 1  # assumes valid above
    next_direction_unbound = curr_direction + next_direction_offset

    if next_direction_unbound >= direction_length:
        next_state_direction_index = next_direction_unbound % direction_length
    elif next_direction_unbound < 0:
        offset_complement = abs(next_direction_unbound) % direction_length
        next_state_direction_index = direction_length - offset_complement
    else:
        next_state_direction_index = next_direction_unbound  # happens to be correct

    return Direction(flag=VALID_DIRECTIONS[next_state_direction_index])
