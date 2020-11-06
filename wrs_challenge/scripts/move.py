#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import sys
import math

rospy.init_node('move')
import utils

if __name__=='__main__':

    try:
        # 視線を少し下げる
        utils.move_head_tilt(-0.4)
    except:
        rospy.logerr('fail to init')
        sys.exit()

    try:
        # 移動姿勢
        utils.move_arm_init()
        # 長テーブルの前に移動
        utils.move_base_goal(1, 0.5, 90)
    except:
        rospy.logerr('fail to move')
        sys.exit()

    try:
        # 把持用初期姿勢に遷移
        utils.move_arm_neutral()
        # 手を開く
        utils.move_hand(1)
        # 黄色のブロックに手を伸ばす（本来はブロックの座標は画像認識すべき）
        utils.move_wholebody_ik(0.9, 1.5, 0.2, 180, 0, 90)
        # 手を下げる
        utils.move_wholebody_ik(0.9, 1.5, 0.08, 180, 0, 90)
        # 手を閉じる
        utils.move_hand(0)
        # 把持用初期姿勢に遷移
        utils.move_arm_neutral()
    except:
        rospy.logerr('fail to grasp')
        sys.exit()

    try:
        # 移動姿勢
        utils.move_arm_init()
        # トレーの前に移動
        utils.move_base_goal(1.8, -0.1, -90)
        # 手を前に動かす
        utils.move_arm_neutral()
        # 手を開く
        utils.move_hand(1)
    except:
        rospy.logerr('fail to move')
        sys.exit()
