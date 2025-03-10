import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoiding Ghosts")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 캐릭터 속성
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# 유령 속성
ghost_size = 50
ghosts = []
ghost_speed = 5
spawn_timer = 0
spawn_interval = 30  # 프레임 단위로 생성

# 스테이지 관리
stage = 1
max_stage = 10

# 점수 및 스테이지 점수 증가 간격
score = 0
score_to_next_stage = 1000

# 이미지 로드
player_image = pygame.image.load("player.png")  # 플레이어 이미지 경로
player_image = pygame.transform.scale(player_image, (player_size, player_size))  # 크기 조정

ghost_image = pygame.image.load("Ghost.png")  # 유령 이미지 경로
ghost_image = pygame.transform.scale(ghost_image, (ghost_size, ghost_size))  # 크기 조정

# 폰트
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
        player_y += player_speed

    # 유령 생성
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        ghost_x = random.randint(0, SCREEN_WIDTH - ghost_size)
        ghosts.append([ghost_x, -ghost_size])
        spawn_timer = 0

    # 유령 이동
    for ghost in ghosts:
        ghost[1] += ghost_speed

    # 충돌 체크
    for ghost in ghosts:
        if (
            player_x < ghost[0] + ghost_size
            and player_x + player_size > ghost[0]
            and player_y < ghost[1] + ghost_size
            and player_y + player_size > ghost[1]
        ):
            running = False

    # 화면 밖으로 나간 유령 제거
    ghosts = [ghost for ghost in ghosts if ghost[1] < SCREEN_HEIGHT]
    score += 1

    # 스테이지 변경
    if score > stage * score_to_next_stage and stage < max_stage:
        stage += 1
        ghost_speed += 1  # 유령 속도 증가
        spawn_interval = max(10, spawn_interval - 5)  # 유령 생성 간격 감소
        player_speed += 0.5  # 플레이어 속도 소폭 증가

    # 플레이어 그리기
    screen.blit(player_image, (player_x, player_y))

    # 유령 그리기
    for ghost in ghosts:
        screen.blit(ghost_image, (ghost[0], ghost[1]))

    # 점수 및 스테이지 표시
    score_text = font.render(f"Score: {score}", True, BLACK)
    stage_text = font.render(f"Stage: {stage}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(stage_text, (10, 40))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
