import Mock from 'mockjs';
import qs from 'query-string';
import setupMock from '@/utils/setupMock';

const { list } = Mock.mock({
  'list|100': [
    {
      termId: /[0-9]{8}[-][0-9]{4}/,
      chnName: () =>
        Mock.Random.pick([
          '手机号码',
          '邮箱',
          '用户ID',
        ]),
      engName: () =>
        Mock.Random.pick([
          'phone number',
          'email',
          'user id',
        ]),
      engAbbr: () =>
        Mock.Random.pick([
          'phnNo',
          'email',
          'usrId',
        ]),
      stdTermFlag: () =>
        Mock.Random.pick([
          true,
          false,
        ]),
    },
  ],
});

setupMock({
  setup: () => {
    Mock.mock(new RegExp('/api/term'), (params) => {
      const {
        page = 1,
        size = 10,
      } = qs.parseUrl(params.url).query;
      const p = page as number;
      const ps = size as number;
      return {
        data: {
          list: list.slice((p - 1) * ps, p * ps),
          total: list.length,
        }
      };
    });
  },
});
