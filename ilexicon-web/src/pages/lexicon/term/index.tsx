import React, { useState, useEffect, useMemo } from 'react';
import { getColumns } from '@/pages/lexicon/term/constants';
import { Button, Card, PaginationProps, Space, Table } from '@arco-design/web-react';
import axios from 'axios';
import Title from '@arco-design/web-react/es/Typography/title';
import styles from '@/pages/list/search-table/style/index.module.less';
import { IconDownload, IconPlus } from '@arco-design/web-react/icon';
import './mock';
import TermSearch from '@/pages/lexicon/term/form';
import { navigate } from '@/utils/route';

function TermTable() {
  const tableCallback = async (record, type) => {
    console.log(record, type);
  };
  const columns = useMemo(() => getColumns(tableCallback), []);
  const [data, setData] = useState([]);
    const [pagination, setPagination] = useState<PaginationProps>({
    sizeCanChange: true,
    showTotal: true,
    pageSize: 10,
    current: 1,
    pageSizeChangeResetCurrent: true,
  });
  const [loading, setLoading] = useState(true);
  const [formParams, setFormParams] = useState({});

  useEffect(() => {
    fetchData();
  }, [pagination.current, pagination.pageSize, JSON.stringify(formParams)]);

  function fetchData() {
    const { current, pageSize } = pagination;
    setLoading(true);
    axios
      .get('/api/term', {
        params: {
          page: current,
          size: pageSize,
          ...formParams,
        },
      })
      .then((res) => {
        setData(res.data.data.list);
        setPagination({
          ...pagination,
          current,
          pageSize,
          total: res.data.total,
        });
        setLoading(false);
      });
  }

  function onChangeTable({ current, pageSize }) {
    setPagination({
      ...pagination,
      current,
      pageSize,
    });
  }

  function handleSearch(params) {
    setPagination({ ...pagination, current: 1 });
    setFormParams(params);
  }

  function handleCreate() {
    navigate('/lexicon/term/edit');
  }

  return (
    <Card>
      <Title heading={6}>用语列表</Title>
      <TermSearch onSearch={handleSearch} />
      <div className={styles['button-group']}>
        <Space>
          <Button type="primary" icon={<IconPlus />} onClick={handleCreate}>
            新建
          </Button>
        </Space>
        {/*<Space>*/}
        {/*  <Button icon={<IconDownload />}>*/}
        {/*    下载*/}
        {/*  </Button>*/}
        {/*</Space>*/}
      </div>
      <Table
        rowKey="id"
        loading={loading}
        onChange={onChangeTable}
        pagination={pagination}
        columns={columns}
        data={data}
      />
    </Card>
  )
}

export default TermTable;