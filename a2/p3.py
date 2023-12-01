import sys, random, grader, parse, math

def random_play_multiple_ghosts(problem):
    #Your p3 code here
    seeds = problem[0]
    layout = problem[1]
    
    ghost_loc = get_ghost_loc(layout)
    pacman_loc = get_pacman_loc(layout)
    foods_loc = get_foods_loc(layout)

    random.seed(seeds, 1)
    solution = 'seed: ' + str(seeds) + '\n'
    solution += '0\n' + convert_map_to_str(layout)
    steps_count = 0
    is_pacman_moving = True
    food_num = len(foods_loc)
    score = 0
    ghost_is_on_food = [False, False, False, False]

    ghost_list = ['W', 'X', 'Y', 'Z']
    ghost_num = 0
    ghost_list = ghost_list[:len(ghost_loc)]
    ghost_is_on_food = ghost_is_on_food[:len(ghost_loc)]
    curr_food = dict()
    
    while True:
        steps_count += 1
        if (is_pacman_moving):
            score += -1
            next_available_direction = get_next_loc(pacman_loc[0], layout)
            next_direction = random.choice(tuple(next_available_direction))
            solution += str(steps_count) + ': P moving ' + str(next_direction) + '\n'
            if (next_direction == 'E'):
                next_item = layout[pacman_loc[0][0]][pacman_loc[0][1] + 1]
                if (next_item in ghost_list):
                    score += -500
                    winner = 'Ghost'
                    ghost = next((item for item in ghost_list if next_item == item), None)
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = ghost
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = 'P'
                    pacman_loc[0][1] += 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break                      
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] + 1] = 'P'
                    pacman_loc[0][1] += 1

            elif (next_direction == 'N'):
                next_item = layout[pacman_loc[0][0] - 1][pacman_loc[0][1]]
                if (next_item in ghost_list):
                    score += -500
                    winner = 'Ghost'
                    ghost = next((item for item in ghost_list if next_item == item), None)
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = ghost
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] -= 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] - 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] -= 1

            elif (next_direction == 'S'):
                next_item = layout[pacman_loc[0][0] + 1][pacman_loc[0][1]]
                if (next_item in ghost_list):
                    score += -500
                    winner = 'Ghost'
                    ghost = next((item for item in ghost_list if next_item == item), None)
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = ghost
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] += 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0] + 1][pacman_loc[0][1]] = 'P'
                    pacman_loc[0][0] += 1
            
            elif (next_direction == 'W'):
                next_item = layout[pacman_loc[0][0]][pacman_loc[0][1] - 1]
                if (next_item in ghost_list):
                    score += -500
                    winner = 'Ghost'
                    ghost = next((item for item in ghost_list if next_item == item), None)
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = ghost
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    score += 10
                    food_num -= 1
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = 'P'
                    pacman_loc[0][1] -= 1
                    if (food_num == 0):
                        score += 500
                        winner = 'Pacman'
                        solution += convert_map_to_str(layout)
                        solution += 'score: ' + str(score) + '\n'
                        solution += 'WIN: ' + winner
                        break
                else:
                    layout[pacman_loc[0][0]][pacman_loc[0][1]] = ' '
                    layout[pacman_loc[0][0]][pacman_loc[0][1] - 1] = 'P'
                    pacman_loc[0][1] -= 1
            is_pacman_moving = False
            solution += convert_map_to_str(layout)
            solution += 'score: ' + str(score) + '\n'

        # Ghost moving
        else:
            curr_ghost_moving = ghost_list[ghost_num]
            next_available_direction = get_next_ghost_loc(ghost_loc[ghost_num], layout)
            if (len(next_available_direction) == 0):
                solution += str(steps_count) + ': ' + str(curr_ghost_moving) + ' moving ' + '\n'
                ghost_num += 1
                if (ghost_num == len(ghost_loc)):
                    is_pacman_moving = True
                    ghost_num = 0
                solution += convert_map_to_str(layout)
                solution += 'score: ' + str(score) + '\n'
                continue

            next_direction = random.choice(tuple(next_available_direction))
            solution += str(steps_count) + ': ' + str(curr_ghost_moving) + ' moving ' + str(next_direction) + '\n'
            if (next_direction == 'E'):
                next_item = layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] + 1]
                
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] + 1] = curr_ghost_moving
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                        ghost_is_on_food[ghost_num] = True
                    curr_food[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] + 1]
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] + 1] = curr_ghost_moving
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] + 1]
                else:
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] + 1] = curr_ghost_moving
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                        ghost_is_on_food[ghost_num] = False
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] + 1]
            
            elif (next_direction == 'N'):
                next_item = layout[ghost_loc[ghost_num][0] - 1][ghost_loc[ghost_num][1]]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    layout[ghost_loc[ghost_num][0] - 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                        ghost_is_on_food[ghost_num] = True
                    curr_food[ghost_num] = [ghost_loc[ghost_num][0] - 1, ghost_loc[ghost_num][1]]
                    layout[ghost_loc[ghost_num][0] - 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0] - 1, ghost_loc[ghost_num][1]]
                else:
                    layout[ghost_loc[ghost_num][0] - 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                        ghost_is_on_food[ghost_num] = False
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0] - 1, ghost_loc[ghost_num][1]]
            
            elif (next_direction == 'S'):
                next_item = layout[ghost_loc[ghost_num][0] + 1][ghost_loc[ghost_num][1]]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    layout[ghost_loc[ghost_num][0] + 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                        ghost_is_on_food[ghost_num] = True
                    curr_food[ghost_num] = [ghost_loc[ghost_num][0] + 1, ghost_loc[ghost_num][1]]
                    layout[ghost_loc[ghost_num][0] + 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0] + 1, ghost_loc[ghost_num][1]]
                else:
                    layout[ghost_loc[ghost_num][0] + 1][ghost_loc[ghost_num][1]] = curr_ghost_moving
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                        ghost_is_on_food[ghost_num] = False
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0] + 1, ghost_loc[ghost_num][1]]
            
            elif (next_direction == 'W'):
                next_item = layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] - 1]
                if (next_item == 'P'):
                    score += -500
                    winner = 'Ghost'
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] - 1] = curr_ghost_moving
                    solution += convert_map_to_str(layout)
                    solution += 'score: ' + str(score) + '\n'
                    solution += 'WIN: ' + winner
                    break
                elif (next_item == '.'):
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                        ghost_is_on_food[ghost_num] = True
                    curr_food[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] - 1]
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] - 1] = curr_ghost_moving
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] - 1]
                else:
                    layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1] - 1] = curr_ghost_moving
                    if (ghost_is_on_food[ghost_num]):
                        layout[curr_food[ghost_num][0]][curr_food[ghost_num][1]] = '.'
                        ghost_is_on_food[ghost_num] = False
                    else:
                        layout[ghost_loc[ghost_num][0]][ghost_loc[ghost_num][1]] = ' '
                    ghost_loc[ghost_num] = [ghost_loc[ghost_num][0], ghost_loc[ghost_num][1] - 1]
                    
            ghost_num += 1
            
            if (ghost_num == len(ghost_loc)):
                is_pacman_moving = True
                ghost_num = 0
            solution += convert_map_to_str(layout)
            solution += 'score: ' + str(score) + '\n'

    return solution

def get_ghost_loc(layout):
    loc = dict()
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == 'W'):
                loc[0] = [row, col]
            elif (cols == 'X'):
                loc[1] = [row, col]
            elif (cols == 'Y'):
                loc[2] = [row, col]
            elif (cols == 'Z'):
                loc[3] = [row, col]
            col += 1
        row += 1
    return loc

def get_pacman_loc(layout):
    loc = []
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == 'P'):
                loc.append([row, col])
            col += 1
        row += 1
    return loc

def get_foods_loc(layout):
    loc = []
    row = 0
    for rows in layout:
        col = 0
        for cols in rows:
            if (cols == '.'):
                loc.append([row, col])
            col += 1
        row += 1
    return loc

def get_next_loc(loc, layout):
    row = loc[0]
    col = loc[1]
    direction = []
    if (layout[row][col + 1] != '%'):
        direction.append('E')
    if (layout[row - 1][col] != '%'):
        direction.append('N')
    if (layout[row + 1][col] != '%'):
        direction.append('S')
    if (layout[row][col - 1] != '%'):
        direction.append('W')
    return direction

def get_next_ghost_loc(loc, layout):
    row = loc[0]
    col = loc[1]
    direction = []
    if (layout[row][col + 1] != '%' and layout[row][col + 1] not in ['W', 'X', 'Y', 'Z']):
        direction.append('E')
    if (layout[row - 1][col] != '%' and layout[row - 1][col] not in ['W', 'X', 'Y', 'Z']):
        direction.append('N')
    if (layout[row + 1][col] != '%' and layout[row + 1][col] not in ['W', 'X', 'Y', 'Z']):
        direction.append('S')
    if (layout[row][col - 1] != '%' and layout[row][col - 1] not in ['W', 'X', 'Y', 'Z']):
        direction.append('W')
    return direction

def convert_map_to_str(layout):
    str = ''
    for rows in layout:
        for cols in rows:
            str += cols
        str += '\n'
    return str

if __name__ == "__main__":
    try: test_case_id = int(sys.argv[1])
    except: test_case_id = -7
    problem_id = 3
    grader.grade(problem_id, test_case_id, random_play_multiple_ghosts, parse.read_layout_problem)