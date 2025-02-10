import React, { useRef, useState } from 'react';
import { FormInstance } from '@arco-design/web-react/es/Form';
import axios from 'axios';
import { Button, Card, Form, Grid, Icon, Input, Message, Space, Tag, Typography } from '@arco-design/web-react';

import styles from './style/index.module.less';

const InputSearch = Input.Search;

function TermEdit() {
  const formRef = useRef<FormInstance>();
  const [loading, setLoading] = useState(false);
  const [words, setWords] = useState<WordItem[]>([]);

  function onSplitWords(text) {
    // TODO 词素分析
    console.log('词素分析文本：', text)
    setWords([{ wordId: '1', chnName: '用户', engName: 'user', engAbbr: 'usr'}, { wordId: '2', chnName: 'ID', engName: 'id', engAbbr: 'id'}]);
  }

  function submit(data) {
    setLoading(true);
    axios
      .post('/api/term', {
        data,
      })
      .then(() => {
        Message.success("提交成功");
      })
      .finally(() => {
        setLoading(false);
      });
  }

  function handleSubmit() {
    formRef.current.validate().then((values) => {
      submit(values);
    });
  }

  function handleReset() {
    formRef.current.resetFields();
  }

  function handleBack() {
    window.history.back();
  }

  return (
    <div className={styles.container}>
      <Form layout="vertical" ref={formRef} className={styles['lexicon-term-edit']}>
        <Card>
          <Typography.Title heading={6}>
            用语参数
          </Typography.Title>
          <Grid.Row gutter={80}>
            <Grid.Col span={8}>
              <Form.Item
                label="中文名称"
                field="chnName"
                rules={[
                  {
                    required: true,
                    message: '请输入用语中文名称',
                  },
                ]}
              >
                <InputSearch placeholder="请输入用语中文名称" searchButton='词素分析' onSearch={onSplitWords} />
              </Form.Item>
            </Grid.Col>
          </Grid.Row>
          <Grid.Row gutter={80}>
            <Grid.Col span={8}>
              <Form.Item
                label="词素结构"
                field="chnName"
                rules={[
                  {
                    required: true,
                    message: '请完成词素分析',
                  },
                ]}
              >
                {
                  words.map(e => <Tag key={e.wordId} size='large' style={{marginRight: '10px'}}>{e.chnName}</Tag>)
                }
              </Form.Item>
            </Grid.Col>
          </Grid.Row>
          <Grid.Row gutter={80}>
            <Grid.Col span={8}>
              <Form.Item
                label="英文名称"
                field="engName"
                rules={[
                  {
                    required: true,
                    message: '请输入用语英文名称',
                  },
                ]}
              >
                {
                  words.map(e => <Tag key={e.wordId} size='large' style={{marginRight: '10px'}}>{e.engName}</Tag>)
                }
              </Form.Item>
            </Grid.Col>
          </Grid.Row>
          <Grid.Row gutter={80}>
            <Grid.Col span={8}>
              <Form.Item
                label="英文缩写"
                field="engAbbr"
                rules={[
                  {
                    required: true,
                    message: '请输入用语英文缩写',
                  },
                ]}
              >
                <Input placeholder='请完成词素分析' value={words.map(e => e.engAbbr).join('')} />
              </Form.Item>
            </Grid.Col>
          </Grid.Row>
        </Card>
      </Form>
      <div className={styles.actions}>
        <Space>
          <Button onClick={handleBack} size="large">
            返回
          </Button>
          <Button onClick={handleReset} size="large">
            重置
          </Button>
          <Button
            type="primary"
            onClick={handleSubmit}
            loading={loading}
            size="large"
          >
            提交
          </Button>
        </Space>
      </div>
    </div>
  )
}

export default TermEdit;