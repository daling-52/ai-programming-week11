import pandas as pd


def 정제(df):
    # 원본 데이터프레임을 보호하기 위해 복사본 생성
    df = df.copy()
    print("시작       ", len(df))

    # 1) 점수가 비어 있는 행 삭제
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거 ", len(df))

    # 2) 모든 열이 완전히 같은 중복 행 제거
    df = df.drop_duplicates()
    print("중복 제거  ", len(df))

    # 3) 반과 과목 문자열의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    # 4) 점수가 0~100 범위를 벗어난 행 삭제
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df


def 반별평균(df):
    # 반별 평균 점수를 소수 둘째 자리까지 반올림하여 반환
    return df.groupby("반")["점수"].mean().round(2)


if __name__ == "__main__":
    raw_df = pd.read_csv("scores_2026.csv")
    clean_df = 정제(raw_df)

    # 필터링: 과목이 '수학'인 행만 남기기
    math_df = clean_df[clean_df["과목"] == "수학"]
    print("\n수학 과목 행 수:", len(math_df))

    # 그룹화 1: 반별 평균
    print("\n[반별 평균]")
    print(반별평균(clean_df))

    # 그룹화 2: 과목 × 반 평균
    print("\n[과목 × 반 평균]")
    print(clean_df.groupby(["과목", "반"])["점수"].mean().round(2))

    # 통계: 반별 개수 · 평균 · 중앙값 · 최댓값
    print("\n[반별 통계 요약]")
    stats = clean_df.groupby("반")["점수"].agg(
        개수="count", 평균="mean", 중앙값="median", 최댓값="max"
    ).round(2)
    print(stats)
