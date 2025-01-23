import { Button, Form, Grid, Input, Select } from '@arco-design/web-react';
import styles from '@/pages/list/search-table/style/index.module.less';
import { IconRefresh, IconSearch } from '@arco-design/web-react/icon';
import React from 'react';


const { Row, Col } = Grid;
const { useForm } = Form;
const colSpan = 8;

function TermSearch(props: {
  onSearch: (values: Record<string, any>) => void;
}) {
    const [form] = useForm();

  const handleSubmit = () => {
    const values = form.getFieldsValue();
    props.onSearch(values);
  };

  const handleReset = () => {
    form.resetFields();
    props.onSearch({});
  };

  return (
    <div className={styles['search-form-wrapper']}>
      <Form
        form={form}
        className={styles['search-form']}
        labelAlign="left"
        labelCol={{ span: 5 }}
        wrapperCol={{ span: 19 }}
      >
        <Row gutter={24}>
          <Col span={colSpan}>
            <Form.Item label='中文名称' field="chnName">
              <Input placeholder='请输入中文名称' allowClear />
            </Form.Item>
          </Col>
          <Col span={colSpan}>
            <Form.Item label='英文名称' field="engName">
              <Input
                allowClear
                placeholder='请输入英文名称'
              />
            </Form.Item>
          </Col>
          <Col span={colSpan}>
            <Form.Item
              label='英文缩写'
              field="engAbbr"
            >
              <Input
                allowClear
                placeholder='请输入英文缩写'
              />
            </Form.Item>
          </Col>
          <Col span={colSpan}>
            <Form.Item
              label='是否标准用语'
              field="filterType"
            >
              <Select
                placeholder='全部'
                options={[
                  {
                    label: '是',
                    value: 'true',
                  },
                  {
                    label: '否',
                    value: 'false',
                  },
                ]}
                allowClear
              />
            </Form.Item>
          </Col>
        </Row>
      </Form>
      <div className={styles['right-button']}>
        <Button type="primary" icon={<IconSearch />} onClick={handleSubmit}>
          查询
        </Button>
        <Button icon={<IconRefresh />} onClick={handleReset}>
          重置
        </Button>
      </div>
    </div>
  );
}

export default TermSearch;